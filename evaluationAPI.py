from flask import Flask, jsonify
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

# Définir le chemin du fichier client_info.json
CLIENT_INFO_FILE_PATH = 'client_info.json'

class EvaluationProprieteResource(Resource):
    def post(self):
        result = evaluer_propriete()
        return jsonify({"message": result})

def evaluer_propriete():
    try:
        with open(CLIENT_INFO_FILE_PATH, 'r', encoding='utf-8') as json_file:
            client_data = json.load(json_file)
    except FileNotFoundError:
        return "Fichier client_info.json introuvable"

    for client_id, client_info in client_data.items():
        # Ici, vous devrez adapter cette partie en fonction de la structure de votre fichier JSON
        indicateur_gaz = client_info.get("indicateur gaz et electricite", "N/A")

        if indicateur_gaz in {'A', 'B', 'C'}:
            client_info["evaluation propriete"] = "Bien evalue"
        else:
            client_info["evaluation propriete"] = "Mal evalue"

    # Enregistrez les résultats dans le fichier client_info.json
    with open(CLIENT_INFO_FILE_PATH, 'w', encoding='utf-8') as json_file:
        json.dump(client_data, json_file, indent=4)

    return "Évaluation de propriété terminée pour le dernier client ajouté"

api.add_resource(EvaluationProprieteResource, '/evaluer_propriete')

if __name__ == '__main__':
    app.run(debug=True, port=5004)
