# DEMO API REST - Università degli Studi di Perugia (Unipg)

## **Sistemi Paralleli e Distribuiti 2022/2023**

Questa demo è composta da:

- Server dell’API: server.py
- Documentazione interattiva: documentazione.js
- 3 Interfacce client per mostrare l’uso dell’API in un ambiente reale: /app (client swagger), client.py (client grafico), index.html (client web)

# Setup:
### Prerequisiti:
È necessario avere installati Node.js, Python e i relativi gestori dei pacchetti (npm, pip).

### GNU/Linux:

#### Ubuntu / Debian:

*   `sudo apt install nodejs python3 npm python3-pip`

#### Fedora / CentOS:

*   `sudo dnf install nodejs python3 npm python3-pip`

#### Arch Linux:

*   `sudo pacman -S nodejs python3 npm python3-pip`

### Windows:

1.  **Node.js**:
    
    *   Vai al sito web ufficiale di Node.js ([https://nodejs.org](https://nodejs.org)).
    *   Scarica il programma di installazione di Node.js per Windows.
    *   Esegui il programma di installazione e segui le istruzioni visualizzate sullo schermo per completare l'installazione.
2.  **Python**:
    
    *   Vai al sito web ufficiale di Python ([https://www.python.org](https://www.python.org)).
    *   Scarica il programma di installazione di Python per Windows.
    *   Esegui il programma di installazione e segui le istruzioni visualizzate sullo schermo per completare l'installazione
3.  **Gestori dei pacchetti**:
    
    *   npm (già incluso nell'installazione di Node.js)
    *   pip (già incluso nell'installazione di Python)

### Mac:

1.  **Node.js**:
    
    *   Vai al sito web ufficiale di Node.js ([https://nodejs.org](https://nodejs.org)).
    *   Scarica il programma di installazione di Node.js per macOS.
    *   Esegui il programma di installazione e segui le istruzioni visualizzate sullo schermo per completare l'installazion.
2.  **Python**:
    
    *   Vai al sito web ufficiale di Python ([https://www.python.org](https://www.python.org)) utilizzando il tuo browser.
    *   Scarica il programma di installazione di Python per macOS.
    *   Esegui il programma di installazione e segui le istruzioni visualizzate sullo schermo per completare l'installazione.
3.  **Gestori dei pacchetti**:
    
    *   npm (già incluso nell'installazione di Node.js).
    *   pip (già incluso nell'installazione di Python)


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

> Se stai utilizzando utilizzando un link che ti è stato condiviso aggiorna l’ultima riga del file **`definizione_openapi.yaml`**
> 

```yaml
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

### Client swagger
```bash
python /app/app.py
```
### Client grafico
```bash
python client.py
```
![Untitled](screen_client.png)

### Client web
file: index.html (doppio click)
