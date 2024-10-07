# Script chamável
import random

def simula_resposta_ia(message):
    res = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(10))
    return res

# print(simula_resposta_ia('prompt'))