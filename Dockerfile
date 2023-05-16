# Dockerfile

# Usa un'immagine di base con Node.js e Python
FROM node:14

# Copia i file documentazione.js e server.py nella directory di lavoro
COPY documentazione.js /app/documentazione.js
COPY server.py /app/server.py

# Imposta la directory di lavoro
WORKDIR /app

# Installa le dipendenze necessarie per i file documentazione.js e server.py
RUN npm install express swagger-ui-express yamljs
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install flask flask_cors pyngrok

# Esponi la porta 80 per il server Express e la porta 5000 per il server Flask
EXPOSE 80
EXPOSE 5000

# Esegui entrambi i server Express e Flask
CMD ["sh", "-c", "node documentazione.js & python server.py"]
