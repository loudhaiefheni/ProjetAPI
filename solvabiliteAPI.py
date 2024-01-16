from flask import Flask, jsonify
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

# Seuil pour évaluer la solvabilité
seuil = 1.5

# Définir le chemin du fichier client_info.json
CLIENT_INFO_FILE_PATH = 'client_info.json'

class SolvabiliteResource(Resource):
    def post(self):
        result = check_solvency()
        return jsonify({"message": result})

def check_solvency():
    try:
        with open(CLIENT_INFO_FILE_PATH, 'r', encoding='utf-8') as json_file:
            client_data = json.load(json_file)
    except FileNotFoundError:
        return "Fichier client_info.json introuvable"

    for client_id, client_info in client_data.items():
        if 'credit_score' in client_info:
            credit_score = client_info['credit_score']
            if credit_score > seuil:
                client_info["Solvabilite"] = "Solvable"
            else:
                client_info["Solvabilite"] = "Non Solvable"

    with open(CLIENT_INFO_FILE_PATH, 'w', encoding='utf-8') as json_file:
        json.dump(client_data, json_file, indent=4)

    return "Solvabilite vérifiée pour le dernier client ajouté"

api.add_resource(SolvabiliteResource, '/check_solvency')

if __name__ == '__main__':
    app.run(debug=True, port=5003)
