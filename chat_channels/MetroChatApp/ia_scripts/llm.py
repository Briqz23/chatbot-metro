# Script chamável
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI
import random

def teste_com_ia(message):
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

# teste_com_ia('oi')


def simula_resposta_ia(message_unica):
    res = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(10))
    return res
