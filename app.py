from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api
from extractionAPI import ExtractionResource
from credit_scoreAPI import CreditScoringResource
from solvabiliteAPI import SolvabiliteResource
from evaluationAPI import EvaluationProprieteResource
from approbationAPI import DecisionApprobationResource
import json, os


app = Flask(__name__)
api = Api(app)


# Utilisateur factice pour cet exemple
fake_user = {"username": "admin", "password": "admin"}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == fake_user['username'] and password == fake_user['password']:
        return render_template('demande.html')
    else:
        return render_template('login.html', message='Identifiants incorrects')

@app.route('/submit_demande', methods=['POST'])
def submit_demande():
    # Récupérer les données du formulaire
    demande_data = request.form['demande_data']

    # Chemin du fichier demande_client.txt
    fichier_demande = 'demande_client.txt'

    # Supprimer l'ancien fichier s'il existe
    if os.path.exists(fichier_demande):
        os.remove(fichier_demande)

    # Écrire les données dans le fichier demande_client.txt
    with open(fichier_demande, 'a', encoding='utf-8') as f:
        f.write(demande_data + '\n')

    return render_template('confirmation.html')



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
    if request.method == 'GET':
        # Traiter la demande lorsque le bouton est cliqué
        try:
            with open(CLIENT_INFO_FILE_PATH, 'r', encoding='utf-8') as json_file:
                client_data = json.load(json_file)
                last_client_id = str(max(int(k) for k in client_data.keys()))
                last_decision = client_data[last_client_id].get("decision_approbation", "N/A")
                return render_template('result.html', decision=last_decision)
        except FileNotFoundError:
            return render_template('error.html', message="Fichier client_info.json introuvable")
    else:
        return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
