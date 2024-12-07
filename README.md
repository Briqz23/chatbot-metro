# Metro Chatbot

[![Assista à demonstração do projeto](https://img.youtube.com/vi/OnSJkpkA6bw/0.jpg)](https://youtu.be/OnSJkpkA6bw)

Este é um projeto para o PI 6, Metro Chatbot, desenvolvido com Python, Django e outras bibliotecas.

## Como iniciar o projeto

### Opção 1: Usando Docker (com Docker Compose)

1. **Instale o Docker e o Docker Compose**:
   - Certifique-se de que o Docker e o Docker Compose estão instalados em sua máquina. Você pode verificar isso executando `docker --version` e `docker-compose --version` no terminal.

2. **Puxe a imagem Docker**:
   - Puxe a imagem mais recente do `chatbot-metro-web` do Docker Hub com o seguinte comando:
     ```bash
     docker pull briqz233/chatbot-metro-web:latest
     ```

3. **Inicie o Docker Compose**:
   - No diretório do projeto, execute o seguinte comando para iniciar os contêineres usando o Docker Compose:
     ```bash
     docker-compose up --build
     ```
   - O comando irá criar e iniciar os contêineres definidos no arquivo `docker-compose.yml` e mapeará as portas adequadamente.

4. **Acesse o servidor**:
   - Abra o navegador e acesse o servidor em: [http://localhost:8000](http://localhost:8000)

---

### Opção 2: Usando Ambiente Virtual (venv)

Se preferir configurar o ambiente localmente, siga os passos abaixo para usar o ambiente virtual:

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
     pip install -r ./requirements.txt
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

---

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
