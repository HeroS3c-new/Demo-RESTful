# Importiamo le librerie necessarie
from flask import Flask, jsonify, request
from flask_cors import CORS
from pyngrok import ngrok
import yaml

# Creiamo un'applicazione Flask
app = Flask(__name__)

# Abilitiamo il CORS per consentire le richieste da qualsiasi origine
CORS(app, resources={r"/*": {"origins": "*"}})

# Definiamo una lista di corsi
corsi = [
    {'id': 1, 'nome': 'Informatica', 'dipartimento': 'Matematica e informatica'},
    {'id': 2, 'nome': 'Giurisprudenza', 'dipartimento': 'Giurisprudenza'},
    {'id': 3, 'nome': 'Ingegneria', 'dipartimento': 'Ingegneria'}
]

# Definiamo una route per ottenere tutti i corsi
@app.route('/corsi', methods=['GET'])
def get_corsi():
    return jsonify(corsi)

# Definiamo una route per ottenere un corso specifico
@app.route('/corsi/<int:corso_id>', methods=['GET'])
def get_corso(corso_id):
    # Cerchiamo il corso nella lista dei corsi
    corso = next((c for c in corsi if c['id'] == corso_id), None)
    if corso is None:
        # Se il corso non è trovato, restituiamo un messaggio di errore e il codice di stato 404 (non trovato)
        return jsonify({'messaggio': 'Corso non trovato'}), 404
    return jsonify(corso)

# Definiamo una route per creare un nuovo corso
@app.route('/corsi', methods=['POST'])
def create_corso():
    nuovo_corso = request.get_json()
    nuovo_corso['id'] = max(c['id'] for c in corsi) + 1
    corsi.append(nuovo_corso)
    return jsonify(nuovo_corso), 201

# Definiamo una route per aggiornare un corso esistente
@app.route('/corsi/<int:corso_id>', methods=['PUT'])
def update_corso(corso_id):
    # Cerchiamo il corso nella lista dei corsi
    corso = next((c for c in corsi if c['id'] == corso_id), None)
    if corso is None:
        # Se il corso non è trovato, restituiamo un messaggio di errore e il codice di stato 404 (non trovato)
        return jsonify({'messaggio': 'Corso non trovato'}), 404
    corso.update(request.get_json())
    return jsonify(corso)

# Definiamo una route per eliminare un corso
@app.route('/corsi/<int:corso_id>', methods=['DELETE'])
def delete_corso(corso_id):
    # Cerchiamo il corso nella lista dei corsi
    corso = next((c for c in corsi if c['id'] == corso_id), None)
    if corso is None:
        # Se il corso non è trovato, restituiamo un messaggio di errore e il codice di stato 404 (non trovato)
        return jsonify({'messaggio': 'Corso non trovato'}), 404
    corsi.remove(corso)
    # Rest

# Questa funzione consente se eseguita di riscrivere automaticamente la lista server in 'definizione_openapi.yaml' con l'URL pubblico di ngrok
# Nota: ngrok rifiuta richieste Cross-Origin su browser da localhost,se si provano ad eseguire richieste dalla documentazione swagger si andrà incontro ad errori. 
# Di default è quindi disabilitata, tutte le richieste effettuate invece direttamente con CURL funzionano correttamente.
def update_openapi_file(file_path, public_url):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    for server in data['servers']:
        server['url'] = public_url.public_url

    with open(file_path, 'w') as file:
        yaml.dump(data, file)

public_url = ngrok.connect(5000)
#update_openapi_file('definizione_openapi.yaml', public_url)
print(f"Public URL: {public_url}")

if __name__ == '__main__':
    app.run()
    
