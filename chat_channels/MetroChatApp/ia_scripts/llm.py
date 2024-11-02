# Script chamável
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI

def simula_resposta_ia(message):
    load_dotenv() 
    client = OpenAI()
    model = ChatOpenAI(
        model='gpt-3.5-turbo-1106',
        temperature=0.7
        )   
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": message
        }
     ]  
    )

    res = (completion.choices[0].message)
    print(str(res))
    return res

simula_resposta_ia('oi')



