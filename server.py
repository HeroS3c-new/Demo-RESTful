from flask import Flask, jsonify, request
from flask_cors import CORS
from pyngrok import ngrok
import os

app = Flask(__name__)
CORS(app)

corsi = [
    {'id': 1, 'nome': 'Informatica', 'dipartimento': 'Matematica e informatica'},
    {'id': 2, 'nome': 'Giurisprudenza', 'dipartimento': 'Giurisprudenza'},
    {'id': 3, 'nome': 'Ingegneria', 'dipartimento': 'Ingegneria'}
]

@app.route('/corsi', methods=['GET'])
def get_corsi():
    return jsonify(corsi)

@app.route('/corsi/<int:corso_id>', methods=['GET'])
def get_corso(corso_id):
    corso = next((c for c in corsi if c['id'] == corso_id), None)
    if corso is None:
        return jsonify({'messaggio': 'Corso non trovato'}), 404
    return jsonify(corso)

@app.route('/corsi', methods=['POST'])
def create_corso():
    nuovo_corso = request.get_json()
    nuovo_corso['id'] = max(c['id'] for c in corsi) + 1
    corsi.append(nuovo_corso)
    return jsonify(nuovo_corso), 201

@app.route('/corsi/<int:corso_id>', methods=['PUT'])
def update_corso(corso_id):
    corso = next((c for c in corsi if c['id'] == corso_id), None)
    if corso is None:
        return jsonify({'messaggio': 'Corso non trovato'}), 404
    corso.update(request.get_json())
    return jsonify(corso)

@app.route('/corsi/<int:corso_id>', methods=['DELETE'])
def delete_corso(corso_id):
    corso = next((c for c in corsi if c['id'] == corso_id), None)
    if corso is None:
        return jsonify({'messaggio': 'Corso non trovato'}), 404
    corsi.remove(corso)
    return '', 204

public_url = ngrok.connect(5000)

print(f"Public URL: {public_url}")

if __name__ == '__main__':
    app.run()
    
