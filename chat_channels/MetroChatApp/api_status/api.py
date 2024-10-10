from bs4 import BeautifulSoup
import requests

def obter_situacao_linhas_metro():
   
    html = requests.get("https://www.metro.sp.gov.br/wp-content/themes/metrosp/direto-metro.php?embed=1").content
    soup = BeautifulSoup(html, 'html.parser')

   
    linha_nomes = soup.find_all('div', class_='linha-nome')
    linha_situacao = soup.find_all('div', class_='linha-situacao')
    linha_numero = soup.find_all('div', class_='linha-numero')

    
    linhas = []
    for numero, nome, situacao in zip(linha_numero, linha_nomes, linha_situacao):
        linha_info = {
            'linha-numero': numero.text.strip(),
            'linha-nome': nome.text.strip(),
            'linha-situacao': situacao.text.strip()
        }
        linhas.append(linha_info)

    
    return linhas


linhas_metro = obter_situacao_linhas_metro()
print(linhas_metro)
for linha in linhas_metro:
    print(linha)
