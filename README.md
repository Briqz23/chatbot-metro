# Metro Chatbot

Este é um projeto para o PI 6, Metro Chatbot, desenvolvido com Python, Django e outras bibliotecas.

## Como iniciar o projeto

1. **Instale o Python**:
   - Certifique-se de que o Python está instalado em sua máquina. Você pode verificar isso executando `python --version` no terminal.

2. **Entre no diretório do projeto**:
   - Navegue até o diretório correto:
     ```bash
     cd chat_channels
     ```
   - Para garantir que você está no diretório certo, use o comando `dir` (ou `ls` no Linux/Mac) e verifique se o arquivo `manage.py` está presente.

3. **Crie um ambiente virtual (venv)**:
   - Caso ainda não tenha um ambiente virtual, crie um com o comando:
     ```bash
     python -m venv venv
     ```

4. **Ative o ambiente virtual**:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

5. **Instale os requerimentos**:
   - Baixe as dependências necessárias executando:
     ```bash
     pip install -r requirements.txt
     ```

6. **Aplique as migrações do banco de dados**:
   - Execute o comando:
     ```bash
     python manage.py migrate
     ```

7. **Inicie o servidor**:
   - Para rodar o servidor de desenvolvimento, use:
     ```bash
     python manage.py runserver
     ```


## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
