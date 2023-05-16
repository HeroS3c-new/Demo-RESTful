# DEMO API REST - Università degli Studi di Perugia (Unipg)

## **Sistemi Paralleli e Distribuiti 2022/2023**

Questa demo è composta da:

- Server dell’API: server.py
- Documentazione interattiva: documentazione.js
- 2 Interfacce client per mostrare l’uso dell’API in un ambiente reale: index.html, client.py

# Setup:

### Dipendenze:

```bash
npm install express swagger-ui-express yamljs
pip install -r requirements.txt
```

## Server API RESTful:

```bash
python server.py
```

> Nota: all’avvio verrà fornito anche un link pubblico attraverso ngrok (utile per essere condiviso con chi non riesce ad effettuare questo passaggio).
> 

> Se stai utilizzando utilizzando il link che ti è stato condiviso aggiorna l’ultima riga del file **`definizione_openapi.yaml`**
> 

```bash
servers:
- url: {url_qui}
```

## Documentazione interattiva:

```bash
node documentazione.js
```

Apri questo link: [http://localhost:3000/](http://localhost:3000/) 

ti ritroverai davanti questa interfaccia: 

![Untitled](Doc.png)

# Opzionale:

Se vuoi testare come le API Rest vengono utilizzate per esporre il modello dati a diverse interfacce

```bash
python client.py
```
![Untitled](screen_client.png)

file: index.html (doppio click)
