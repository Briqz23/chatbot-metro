import numpy as np
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_community.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.utils.math import cosine_similarity
from .data.templates import (
    rotas_perguntas,
    horarios_perguntas,
    politicas_perguntas,
    system_rotas_template,
    system_horarios_template,
    system_politicas_template,
)
from langchain.schema import Document

load_dotenv()

def gerando_data():
    # Diretório do arquivo atual (llm.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Caminho para o arquivo scrapping_metro.txt
    file_path = os.path.join(current_dir, 'data', 'scrapping_metro.txt')

    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)

    with open(file_path, "r", encoding="utf-8") as f:
        docs = f.read()

    document = Document(page_content=docs)

    # Agora você pode usar o splitter
    splitted_data = splitter.split_documents([document])  # Passa uma lista de documentos

    return splitted_data

import numpy as np
import faiss
import os

def gerando_embedding(splitted_data):
    embedding = OpenAIEmbeddings()

    # Caminho relativo para salvar o índice FAISS e os embeddings das perguntas
    base_path = os.path.join(os.path.dirname(__file__), "data")
    faiss_index_path = os.path.join(base_path, "faiss_index")
    rotas_embeddings_path = os.path.join(base_path, "rotas_embeddings.npy")
    horarios_embeddings_path = os.path.join(base_path, "horarios_embeddings.npy")
    politicas_embeddings_path = os.path.join(base_path, "politicas_embeddings.npy")

    # Certifique-se de que o diretório "data" existe antes de salvar
    os.makedirs(base_path, exist_ok=True)

    # Verificar e carregar o índice FAISS ou criar um novo
    if os.path.exists(faiss_index_path) and os.path.isfile(f"{faiss_index_path}.index"):
        vectorStore = FAISS.load_local(faiss_index_path, embedding)
    else:
        vectorStore = FAISS.from_documents(splitted_data, embedding)
        vectorStore.save_local(faiss_index_path)

    # Carregar ou gerar embeddings específicos para as perguntas
    if all(os.path.exists(path) for path in [rotas_embeddings_path, horarios_embeddings_path, politicas_embeddings_path]):
        rotas_perguntas_embeddings = np.load(rotas_embeddings_path)
        horarios_perguntas_embeddings = np.load(horarios_embeddings_path)
        politicas_perguntas_embeddings = np.load(politicas_embeddings_path)
    else:
        rotas_perguntas_embeddings = embedding.embed_documents(rotas_perguntas)
        horarios_perguntas_embeddings = embedding.embed_documents(horarios_perguntas)
        politicas_perguntas_embeddings = embedding.embed_documents(politicas_perguntas)
        
        # Salvar embeddings em arquivos
        np.save(rotas_embeddings_path, rotas_perguntas_embeddings)
        np.save(horarios_embeddings_path, horarios_perguntas_embeddings)
        np.save(politicas_embeddings_path, politicas_perguntas_embeddings)

    retriever = vectorStore.as_retriever(search_kwargs={"k": 5})

    return (
        retriever,
        rotas_perguntas_embeddings,
        horarios_perguntas_embeddings,
        politicas_perguntas_embeddings,
    )

def prompt_router(
    embeddings,
    input,
    rotas_perguntas_embeddings,
    horarios_perguntas_embeddings,
    politicas_perguntas_embeddings,
):
    query_embedding = embeddings.embed_query(input["query"])

    rotas_similarity = cosine_similarity([query_embedding], rotas_perguntas_embeddings)[0]
    horarios_similarity = cosine_similarity([query_embedding], horarios_perguntas_embeddings)[0]
    politicas_similarity = cosine_similarity([query_embedding], politicas_perguntas_embeddings)[0]

    max_similarity = max(
        max(rotas_similarity), max(horarios_similarity), max(politicas_similarity)
    )

    if max_similarity == max(rotas_similarity):
        template = system_rotas_template
    elif max_similarity == max(horarios_similarity):
        template = system_horarios_template
    else:
        template = system_politicas_template

    return f"{template}\n\nUsuário: {input['query']}" 


def simula_resposta_ia(message, chat_history):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    model = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.7)

    formatted_history = [{"role": msg["role"], "content": msg["content"]} for msg in chat_history["chat_history"]]
    
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você está falando com um assistente virtual."},
            {"role": "user", 
             "content": f"""
                    CONSIDERANDO O SEGUINTE HISTÓRIO DE MENSAGENS:
                    {formatted_history}
                    RESPONDA A MENSAGEM DO USUÁRIO:
                    {message}

                """
},  # Mensagem do usuário
        ],
    )

    res = completion.choices[0].message.content
    return res

    # Formate o histórico para o modelo da IA
    
    # Obtenha a resposta da IA, considerando o contexto
    #resposta = obter_resposta_ia({"query": chat_data["chat_history"][-1]["content"], "history": formatted_history})

def get_input_query(message):
    return {"query": message}


def obter_resposta_ia(message, chat_history):
    # Gerar dados e embeddings
    splitted_data = gerando_data()
    (
        retriever,
        rotas_perguntas_embeddings,
        horarios_perguntas_embeddings,
        politicas_perguntas_embeddings,
    ) = gerando_embedding(splitted_data)

    # Obter a consulta de entrada
    input_query = get_input_query(message)

    # Roteamento do prompt
    template = prompt_router(
        OpenAIEmbeddings(),
        input_query,
        rotas_perguntas_embeddings,
        horarios_perguntas_embeddings,
        politicas_perguntas_embeddings,
    )

    # Simulação de resposta da IA
    response = simula_resposta_ia(template, chat_history)

    return response
