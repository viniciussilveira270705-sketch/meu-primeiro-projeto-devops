FROM python:3.9-slim

WORKDIR /app

COPY estudo.txt .

CMD ["cat", "estudo.txt"]
