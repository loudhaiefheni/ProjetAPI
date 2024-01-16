from flask import Flask, render_template
from flask_restful import Api
from extractionAPI import ExtractionResource
from credit_scoreAPI import CreditScoringResource
from solvabiliteAPI import SolvabiliteResource
from evaluationAPI import EvaluationProprieteResource
from approbationAPI import DecisionApprobationResource
import json


app = Flask(__name__)
api = Api(app)

# Définir le chemin du fichier client_info.json
CLIENT_INFO_FILE_PATH = 'client_info.json'

# Ajouter les ressources aux routes Flask-RESTful
api.add_resource(ExtractionResource, '/extract_data')
api.add_resource(CreditScoringResource, '/calculate_credit_score')
api.add_resource(SolvabiliteResource, '/check_solvency')
api.add_resource(EvaluationProprieteResource, '/evaluer_propriete')
api.add_resource(DecisionApprobationResource, '/prendre_decision_approbation')

# Route pour afficher la décision d'approbation dans une page HTML
@app.route('/afficher_decision_approbation', methods=['GET', 'POST'])
def afficher_decision_approbation():
    try:
        with open(CLIENT_INFO_FILE_PATH, 'r', encoding='utf-8') as json_file:
            client_data = json.load(json_file)
            last_client_id = str(max(int(k) for k in client_data.keys()))
            last_decision = client_data[last_client_id].get("decision_approbation", "N/A")
            return render_template('result.html', decision=last_decision)
    except FileNotFoundError:
        return render_template('error.html', message="Fichier client_info.json introuvable")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
