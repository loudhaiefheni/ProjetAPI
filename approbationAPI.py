from flask import Flask, jsonify
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

# Définir le chemin du fichier client_info.json
CLIENT_INFO_FILE_PATH = 'client_info.json'

class DecisionApprobationResource(Resource):
    def post(self):
        results = prendre_decision()
        return jsonify({"message": results})

def prendre_decision():
    try:
        with open(CLIENT_INFO_FILE_PATH, 'r', encoding='utf-8') as json_file:
            client_data = json.load(json_file)
    except FileNotFoundError:
        return "Fichier client_info.json introuvable"

    for client_id, client_info in client_data.items():
        solvabilite = client_info.get("Solvabilite", "N/A")
        evaluation_propriete = client_info.get("evaluation propriete", "N/A")

        if solvabilite == "Solvable" and evaluation_propriete == "Bien evalue":
            client_info["decision_approbation"] = "Positif"
        else:
            client_info["decision_approbation"] = "Negatif"

    # Enregistrez les résultats dans le fichier client_info.json
    with open(CLIENT_INFO_FILE_PATH, 'w', encoding='utf-8') as json_file:
        json.dump(client_data, json_file, indent=4)

    return "Décisions d'approbation ajoutées au dernier client ajouté"

api.add_resource(DecisionApprobationResource, '/prendre_decision_approbation')

if __name__ == '__main__':
    app.run(debug=True, port=5005)
