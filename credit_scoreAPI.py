from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)

# Définir le chemin des fichiers
CLIENT_INFO_FILE_PATH = 'client_info.json'
CREDIT_DATA_FILE_PATH = 'credit_data.json'

class CreditScoringResource(Resource):
    def post(self):
        calculate_score()

        return jsonify({"message": f"Score de crédit calculé pour le dernier client "})

def calculate_score():
    credit_data = load_credit_data(CREDIT_DATA_FILE_PATH)  # Charger les données de crédit
    client_info = load_info_file(CLIENT_INFO_FILE_PATH)

    for client_id, client_data in credit_data.items():
        credit_score = calculate_credit_score(client_data)
        if client_id in client_info:
            client_info[client_id]["credit_score"] = credit_score

    save_credit_data(CLIENT_INFO_FILE_PATH, client_info)

def calculate_credit_score(client_data):
    if 'requests' in client_data and 'delays' in client_data and 'bankruptcies' in client_data:
        return 0.5 * client_data['requests'] - 0.2 * client_data['delays'] + 0.3 * client_data['bankruptcies']
    return 0.0

def load_info_file(client_info_file):
    try:
        with open(client_info_file, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        # Gérer l'erreur de fichier non trouvé
        return {}

def load_credit_data(client_data_file):
    try:
        with open(client_data_file, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        # Gérer l'erreur de fichier non trouvé
        return {}

def save_credit_data(client_info_file, data):
    with open(client_info_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

api.add_resource(CreditScoringResource, '/calculate_credit_score')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
