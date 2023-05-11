# DEMO API REST - Università degli Studi di Perugia (Unipg)
## Sistemi Paralleli e Distribuiti 2022/2023

## Endpoint `/corsi`

### `GET /corsi`

Restituisce la lista di tutti i corsi offerti dall'Università degli Studi di Perugia.

**Esempio di risposta:**

```json
[
    {
        "id": 1,
        "nome": "Informatica",
        "dipartimento": "Matematica e informatica"
    },
    {
        "id": 2,
        "nome": "Giurisprudenza",
        "dipartimento": "Giurisprudenza"
    },
    {
        "id": 3,
        "nome": "Ingegneria",
        "dipartimento": "Ingegneria"
    }
]
```

### `GET /corsi/{id}`

Dettagli singolo corso 
**Parametri:**
- `id` (int) - L'ID del corso

**Esempio di risposta:**

```json
[
{
    "id": 1,
    "nome": "Informatica",
    "dipartimento": "Matematica e informatica"
}
]
```


### `POST /corsi`

Crea un nuovo corso 
**Parametri:**
- `nome` (string) - nome del corso
- `dipartimento` (string) - facolta del corso

**Esempio di richiesta:**

```json
[
{
    "nome": "Economia",
    "dipartimento": "Economia"
}

]
```

## Client locale
`python client.py`
![client](screen_client.png)
