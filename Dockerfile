# Usa a imagem oficial enxuta baseada no Python 3.13 do seu ambiente local
FROM python:3.13-slim

# Define o diretório interno onde o app vai viver dentro do container
WORKDIR /app

# Copia e instala dependências antes do código para otimizar o cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia toda a estrutura do projeto para dentro do contêiner
COPY . .

# Cria as pastas de persistência caso não existam no mapeamento
RUN mkdir -p logs vault_storage

# Por padrão, o container liga direto no modo Sentinela (tempo real)
CMD ["python", "watcher.py"]