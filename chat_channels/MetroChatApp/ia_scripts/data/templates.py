system_rotas_template = """
        Adapte à linguagem de quem está falando com você. Se alguém falar em inglÊs, responda em inglês. \
        Você só resposnde perguntas relacionadas ao metrô de São Paulo. \
        Você é um especialista no sistema de Metrô de São Paulo em rotas. \
        Você tem amplo conhecimento sobre as linhas do metrô, suas interligações e horários de pico, fornecendo alternativas rápidas e eficientes para quem utiliza o metrô. \
        Responda em ate 15 palavras, com informações claras e precisas.

    """

system_horarios_template = """
        Adapte à linguagem de quem está falando com você. Se alguém falar em inglÊs, responda em inglês. \
        Você só resposnde perguntas relacionadas ao metrô de São Paulo. \
        Você é um especialista em atualizações sobre o sistema de Metrô de São Paulo. \
        Você informa sobre greves, interrupções e atrasos, além de conhecer detalhadamente os horários de operação do metrô. \
        Você sugere opções alternativas para os passageiros durante períodos de interrupção do serviço. \
        Responda em ate 15 palavras, com informações claras e precisas.
 

"""

system_politicas_template = """
        Adapte à linguagem de quem está falando com você. Se alguém falar em inglÊs, responda em inglês. \
        Adapte à linguagem de quem está falando com você. \
        Você só resposnde perguntas relacionadas ao metrô de São Paulo. \
        Você é um especialista em políticas públicas relacionadas ao sistema de Metrô de São Paulo. \
        Você tem conhecimento detalhado sobre as leis, regulamentos e iniciativas que afetam o metrô, e oferece respostas claras \
        e baseadas em fatos sobre como essas políticas impactam os passageiros. \
        Responda em ate 15 palavras, com informações claras e precisas.

        """

rotas_perguntas = [
    "Qual é a rota mais rápida da estação Sé até a estação Vila Madalena?",
    "Como posso evitar as estações mais lotadas durante o horário de pico?",
    "Quais são as melhores conexões entre as linhas azul e verde do metrô?",
]

horarios_perguntas = [
    "Há alguma greve no Metrô de São Paulo programada para esta semana?",
    "O metrô está funcionando normalmente durante o feriado?",
    "Quais são os horários de operação do metrô aos domingos?",
]

politicas_perguntas = [
    "Quais são as políticas de acessibilidade nas estações do Metrô de São Paulo?",
    "Como as tarifas do metrô são decididas e ajustadas?",
    "Quais são as políticas de sustentabilidade adotadas pelo Metrô de São Paulo?",
]


metro_scrapping = """
Situação das Linhas do Metrô:
Linha: 1 - Azul
Situação: Operação Normal
--------------------------------------------------------------------------------
Linha: 2 - Verde
Situação: Operação Normal
--------------------------------------------------------------------------------
Linha: 3 - Vermelha
Situação: Operação Normal
--------------------------------------------------------------------------------
Linha: 4 - Amarela
Situação: Operação Normal
--------------------------------------------------------------------------------
Linha: 5 - Lilás
Situação: Operação Normal
--------------------------------------------------------------------------------
Linha: 15 - Prata
Situação: Operação Normal
--------------------------------------------------------------------------------
Última atualização: 30-10-2024 22:22:09

Perguntas Frequentes do Metrô:
Pergunta: 1. Ocorreu um problema no Metrô e cheguei atrasado ao trabalho. É possível uma declaração para justificar atrasos no trabalho (ou demais compromissos)?
Resposta: Sim! Caso a ocorrência tenha sido no dia de hoje, nas linhas 1-Azul, 2-Verde, 3-Vermelha ou 15-Prata, acesseesse linke faça o download da declaração de ocorrência.Caso a ocorrência tenha sido em um outro dia, pedimos que abra uma solicitação noFale Conosco.Para ocorrências na Linha 4-Amarela, solicite àconcessionária Via Quatro. Para ocorrências nas Linha 5-Lilás, Linha 8-Diamante ou 9-Esmeralda solicite aoConsórcio Via Mobilidade. Para ocorrências nas demais linhas, acessoo site da CPTM (Companhia Paulista de Trens Metropolitanos).
--------------------------------------------------------------------------------
Pergunta: 2. Presenciei uma ocorrência de segurança pública ou emergência no Metrô. Como devo proceder?
Resposta: Envie um SMS para o serviço do SMS Segurança (97333-2252) ou baixe o aplicativo Metrô Conecta,     disponível paraAndroideiPhone.Você também pode comunicar a ocorrência para qualquer empregado que estiver disponível nas estações.
--------------------------------------------------------------------------------
Pergunta: 3. Encontrei um lugar ou equipamento sujo ou com problemas. Como devo proceder?
Resposta: Você pode:Informar o empregado da estação.Usar o aplicativo Metrô Conecta, disponível paraAndroideiPhone.Ligar para a Central de Informações, pelo telefone 0800-7707722, que está disponível todos os
        dias, das 5h à meia-noite.Agradecemos por colaborar com a manutenção da qualidade dos nossos serviços!
--------------------------------------------------------------------------------
Pergunta: 4. Como faço para trabalhar ou estagiar no Metrô?
Resposta: Solicitamos que acesseesse linkpara mais informações.
--------------------------------------------------------------------------------
Pergunta: 5. Como faço para obter mais informações sobre bilhetes ou tarifas
Resposta: Solicitamos que acesseesse
    linkpara mais informações.
--------------------------------------------------------------------------------
Pergunta: 6. Muitas vezes, quero ir a lugares próximos às estações do Metrô e não sei como chegar no destino. A quem devo recorrer?
Resposta: Para ajudar os passageiros na escolha do melhor percurso pela Rede Metropolitana de Transportes, o Metrô de São Paulo disponibiliza o Sistema de Trajetos, que informa todo o percurso desde a estação de embarque até a estação de desembarque, indicando o melhor caminho em tempo e dinheiro. A consulta, que inclui estações do Metrô, CPTM e Terminais da EMTU, pode ser realizada de duas maneiras: ou por uma lista de estações ou através de um mapa em que o passageiro indica a origem e o destino. O serviço também indica o horário de funcionamento das estações e o tempo estimado para a realização do percurso. O resultado das buscas feitas pelos passageiros através do Sistema de Trajetos do Metrô exibe, ainda, o Mapa dos Arredores, que mostra os pontos de interesse próximos às estações.Consulte oSistema de Trajetosdo Metrô em parceria com o Moovit.Esclarecemos que informações sobre itinerários também são fornecidas pela nossa Área de Atendimento ao Passageiro, que atende pelo telefone 0800-7707722, todos os dias, das das 5h00 à meia-noite ou ainda noFale Conoscodo site. Os funcionários das estações também podem ajudar nessas situações.
--------------------------------------------------------------------------------
Pergunta: 7. Sou professor(a) e quero levar meus alunos para conhecer o Metrô. Como devo proceder?
Resposta: Os interessados devem acessar o nosso site para conhecer o Programa “Turma do Metrô“.
--------------------------------------------------------------------------------
Pergunta: 8. Sei que o Metrô atende às escolas, só que não sou estudante e tenho curiosidade em conhecer o Centro de Controle Operacional. Existe essa possibilidade?
Resposta: Sim. Há um programa chamado “Conheça seu Metrô” em que o passageiro poderá visitar uma estação, conhecer a cabine de um trem e ver como funciona o Centro de Controle Operacional.O interessado deve preencher oformulário eletrônicodisponível no nosso site. Assim que um grupo é montado, todos são avisados sobre data/horário/local. O evento acontece aos sábados.
--------------------------------------------------------------------------------
Pergunta: 9. Quero entender porque em algumas ocasiões, principalmente nos horários de pico, as estações da Linha 3-Vermelha funcionam com menos bloqueios para embarque e mais para desembarque.
Resposta: O Metrô de São Paulo esclarece que eventuais filas nos bloqueios de entrada da Linha 3-Vermelha são uma estratégia para controlar o fluxo de passageiros nas plataformas, proporcionando maior segurança aos passageiros.Com esse controle, pode-se, inclusive, dar maior velocidade aos trens. A liberação desordenada de passageiros causa comprovadamente acúmulo nas plataformas e atraso nos trens, já que é preciso um tempo de parada maior, com aumento do risco de acidentes.
--------------------------------------------------------------------------------
Pergunta: 10. Preciso fazer um trabalho escolar e quero saber onde obtenho informações e publicações a respeito do Metrô.
Resposta: É necessário que faça o pedido pelo canal “SIC” do Metrô-SP. É só clicar no link abaixo e acessar a página doServiços de Informação ao Cidadão.
--------------------------------------------------------------------------------
Pergunta: 11. Qual a estação mais próxima do Aeroporto de Congonhas? Como faço para chegar?
Resposta: A Estação São Judas da Linha 1-Azul, é a mais próxima do Aeroporto de Congonhas (cerca de 3km).Na Estação São Judas há linhas de ônibus que passam pelo Aeroporto, sugerimos: 675I – Terminal João Dias
--------------------------------------------------------------------------------
Pergunta: 12. Como faço para chegar ao Aeroporto Internacional de Guarulhos?
Resposta: Existem as seguintes opções de itinerários para o Aeroporto de Guarulhos:Por linhas de trem da CPTMExpresso Aeroporto Embarque pela estação Luz sentido Aeroporto-Guarulhos. Saída todos os dias, das 5h00 à meia-noite, de hora em hora.Linha 13 – Jade Embarque pela estação Engº Goulart (transferência pela Linha 12 – Safira da CPTM). Saídas todos os dias, das 4h00 à meia-noite. Para conferir mais informações a respeito dos horários dos trens da CPTM para o Aeroporto, acesse:https://www.cptm.sp.gov.br/sua-viagem/Pages/AeroportoPor ônibusLinha suburbana da EMTU: Embarque pelo terminal de ônibus norte do Tatuapé e pegue a linha 257Confira os horários de saídas e itinerário detalhado acessando o link:https://www.emtu.sp.gov.br/emtu/itinerarios-e-tarifas/encontre-uma-linha/pelo-numero-da-linha.fss?numlinha=257&pag=buscanumero.htmAirport Bus Service (ônibus executivo):258 – Aeroporto de Congonhas316 – Circuito de Hotéis472 – Terminal Rodoviário Barra FundaPara mais informações sobre o itinerário das linhas executivas, acesse o a página de Itineráriosno site da EMTU.
--------------------------------------------------------------------------------
Pergunta: 13. Como faço para fornecer produtos e serviços ao Metrô?
Resposta: Na página deLicitações, há o procedimento para o cadastro de fornecedores, avisos e editais. Informações complementares podem ser obtidas no Departamento de Licitações pelo telefone(11) 3291-5435
--------------------------------------------------------------------------------
Pergunta: 14. Como faço para montar uma loja nas estações do Metrô?
Resposta: Para uso de espaço comercial no Metrô favor acessareste link.Também pode entrar em contato com a gerência responsável pelo do e-mail: comercial@metrosp.com.br ou pelo telefone (11) 3291-3929.
--------------------------------------------------------------------------------

Informações do Achados e Perdidos:
/governosp
--------------------------------------------------------------------------------
/governosp
--------------------------------------------------------------------------------
Um dos serviços mais respeitados oferecido pelo Metrô de São Paulo é o Achados e Perdidos, que existe desde 1975.
--------------------------------------------------------------------------------
O sistema de busca, via Internet, foi criado para localizar objetos perdidos no sistema e guardá-los para o passageiro poder procurar. No caso de documentos, a consulta também pode ser feita através da Central de Informações no telefone 0800-7707722, todos os dias, das 5h00 à meia-noite.
--------------------------------------------------------------------------------
O Posto Central de Achados e Perdidos funciona na Estação Sé, de 2ª a 6ª, das 7h00 às 20h00, exceto feriados.
--------------------------------------------------------------------------------
Os objetos ficam guardados à disposição dos interessados por 60 dias. Os itens não procurados são encaminhados para o Fundo Social de Solidariedade do Estado de São Paulo, e os documentos para os órgãos emissores.
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------



"""