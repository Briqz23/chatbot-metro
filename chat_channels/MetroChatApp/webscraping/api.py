from bs4 import BeautifulSoup
import requests
from datetime import datetime

def obter_informacoes_metro():
    html_faq = requests.get("https://www.metro.sp.gov.br/fale-conosco/faq/").content
    soup_faq = BeautifulSoup(html_faq, 'html.parser')

    perguntas_faq = soup_faq.find_all('button', class_='accordion-button')

    perguntas_respostas = []
    for pergunta in perguntas_faq:
        resposta_id = pergunta['data-bs-target']
        resposta_div = soup_faq.select_one(resposta_id)

        if resposta_div:
            resposta_texto = resposta_div.get_text(strip=True)
        else:
            resposta_texto = "Resposta não encontrada."

        faq_metro = {
            'pergunta': pergunta.text.strip(),
            'resposta': resposta_texto
        }

        perguntas_respostas.append(faq_metro)

    
    html_achados = requests.get("https://www.metro.sp.gov.br/sua-viagem/achados-perdidos/").content
    soup_achados = BeautifulSoup(html_achados, 'html.parser')

    achados_textos = soup_achados.find_all('p')
    achados_info = []

    for texto in achados_textos:
        achados_info.append(texto.get_text(strip=True))

    return perguntas_respostas, achados_info

def obter_status_metro():
    with requests.Session() as session:
        response = session.get("https://www.metro.sp.gov.br/wp-content/themes/metrosp/direto-metro.php?embed=1")

    soup_linhas = BeautifulSoup(response.content, 'html.parser')
    hora_request = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    linhas = []
    for linha_info in soup_linhas.select('.linha'):
        numero = linha_info.select_one('.linha-numero').text.strip()
        nome = linha_info.select_one('.linha-nome').text.strip()
        situacao = linha_info.select_one('.linha-situacao').text.strip()

        linha_dados = {
            'linha_numero': numero,
            'linha_nome': nome,
            'linha_situacao': situacao
        }
        linhas.append(linha_dados)

    return linhas, hora_request

faq_metro, achados_info = obter_informacoes_metro()
linhas, hora_agora = obter_status_metro()

with open('MetroChatApp/ia_scripts/informacoes_metro.txt', 'w', encoding='utf-8') as file:
    file.write("Situação das Linhas do Metrô:\n")
    for linha in linhas:
        file.write(f"Linha: {linha['linha_numero']} - {linha['linha_nome']}\n")
        file.write(f"Situação: {linha['linha_situacao']}\n")
        file.write('-' * 80 + '\n')
    file.write(f"Última atualização: {hora_agora}\n")

    file.write("\nPerguntas Frequentes do Metrô:\n")
    for faq in faq_metro:
        file.write(f"Pergunta: {faq['pergunta']}\n")
        file.write(f"Resposta: {faq['resposta']}\n")
        file.write('-' * 80 + '\n')

    file.write("\nInformações do Achados e Perdidos:\n")
    for achado in achados_info:
        file.write(f"{achado}\n")
        file.write('-' * 80 + '\n')

print("Arquivo 'informacoes_metro.txt' criado com sucesso na pasta ia_scripts.")
