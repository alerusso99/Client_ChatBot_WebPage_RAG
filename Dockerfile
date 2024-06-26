# Base Image
FROM python:3.10

# Imposta la directory di lavoro
WORKDIR /chatBot_app

# Copia i requisiti
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice sorgente
COPY . .

# Esponi la porta
EXPOSE 8502

# Comando da eseguire all'avvio del container
CMD ["streamlit", "run", "eseguibile_chatbot.py"]