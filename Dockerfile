FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip uninstall -y channels daphne redis

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -U 'channels[daphne]'

COPY . .

WORKDIR /app/chat_channels

EXPOSE 8080

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"]
