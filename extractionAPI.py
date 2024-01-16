from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)

class ExtractionResource(Resource):
    def post(self):
        # Extraire les données du fichier texte
        new_data = extract_data()

        # Charger les données existantes depuis le fichier JSON (s'il existe)
        try:
            with open('client_info.json', 'r', encoding='utf-8') as json_file:
                existing_data = json.load(json_file)
        except FileNotFoundError:
            existing_data = {}

        # Obtenir le prochain identifiant unique
        unique_id = len(existing_data)

        # Stocker les nouvelles données sous l'identifiant unique
        existing_data[unique_id] = new_data

        # Convertir les données fusionnées en format JSON
        json_data = json.dumps(existing_data, indent=4)

        # Écrire le JSON dans le fichier
        with open('client_info.json', 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)

        return jsonify({"message": f"Nouvelles données extraites et ajoutées à client_info.json avec l'ID {unique_id}"})


def extract_data():
    with open('demande_client.txt', 'r', encoding='utf-8') as f:
        new_data_content = f.read()

    lines = new_data_content.split("\n")
    new_data = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(":", 1)
            new_data[key.strip()] = value.strip()

    return new_data

api.add_resource(ExtractionResource, '/extract_data')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
