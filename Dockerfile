# Dockerfile

# Usa un'immagine di base con Node.js
FROM node:14

# Copia il file documentazione.js nella directory di lavoro
COPY documentazione.js /app/documentazione.js

# Imposta la directory di lavoro
WORKDIR /app

# Installa le dipendenze necessarie per il file documentazione.js
RUN npm install express swagger-ui-express yamljs

# Copia il file server.py nella directory di lavoro
COPY server.py /app/server.py

# Installa le dipendenze necessarie per il file server.py
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install flask flask_cors pyngrok

# Esponi la porta 80 per il server Express
EXPOSE 80

# Esegui il server Express e il server Flask
CMD ["node", "documentazione.js"]


# Dockerfile per il server Flask
# Usa un'immagine di base con Python
FROM python:3.9

# Copia il file server.py nella directory di lavoro
COPY server.py /app/server.py

# Imposta la directory di lavoro
WORKDIR /app

# Installa le dipendenze necessarie per il file server.py
RUN pip install flask flask_cors pyngrok

# Esponi la porta 5000 per il server Flask
EXPOSE 5000

# Esegui il server Flask
CMD ["python", "server.py"]
