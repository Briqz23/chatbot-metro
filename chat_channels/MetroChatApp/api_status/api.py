from bs4 import BeautifulSoup
import requests

def obter_informacoes_metro():
    html_linhas = requests.get("https://www.metro.sp.gov.br/wp-content/themes/metrosp/direto-metro.php?embed=1").content
    soup_linhas = BeautifulSoup(html_linhas, 'html.parser')

    linha_nomes = soup_linhas.find_all('div', class_='linha-nome')
    linha_situacao = soup_linhas.find_all('div', class_='linha-situacao')
    linha_numero = soup_linhas.find_all('div', class_='linha-numero')

    linhas = []
    for numero, nome, situacao in zip(linha_numero, linha_nomes, linha_situacao):
        linha_info = {
            'linha-numero': numero.text.strip(),
            'linha-nome': nome.text.strip(),
            'linha-situacao': situacao.text.strip()
        }
        linhas.append(linha_info)

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

    return linhas, perguntas_respostas, achados_info


situacao_linhas, faq_metro, achados_info = obter_informacoes_metro()

with open('MetroChatAPP/ia_scripts/informacoes_metro.txt', 'w', encoding='utf-8') as file:
    file.write("Situação das Linhas do Metrô:\n")
    for linha in situacao_linhas:
        file.write(f"Linha: {linha['linha-numero']} - {linha['linha-nome']}\n")
        file.write(f"Situação: {linha['linha-situacao']}\n")
        file.write('-' * 80 + '\n')

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
