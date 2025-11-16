FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# pg_isready está no pacote postgresql-client
RUN apt-get update && apt-get install -y postgresql-client

COPY . .

RUN chmod +x esperar_banco.sh

CMD ["./esperar_banco.sh", "db", "python", "app.py"]
