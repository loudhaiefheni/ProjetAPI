from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api, Resource
from extractionAPI import ExtractionResource
from credit_scoreAPI import CreditScoringResource
from solvabiliteAPI import SolvabiliteResource
from evaluationAPI import EvaluationProprieteResource
from approbationAPI import DecisionApprobationResource
import json, os

app = Flask(__name__)
api = Api(app)

# Définir le chemin du fichier client_info.json
CLIENT_INFO_FILE_PATH = 'client_info.json'


# Définir les ressources Flask-RESTful
class AfficherDecisionApprobationResource(Resource):
    def post(self):
        # Traitement de la demande lorsque le bouton est cliqué
        try:
            # Appel à l'API d'extraction
            extract_response = ExtractionResource().post()

            # Appel à l'API de scoring de crédit
            credit_score_response = CreditScoringResource().post()

            # Appel à l'API de solvabilité
            solvabilite_response = SolvabiliteResource().post()

            # Appel à l'API d'évaluation de propriété
            eval_propriete_response = EvaluationProprieteResource().post()

            # Appel à l'API de décision d'approbation
            decision_response = DecisionApprobationResource().post()
            
            
            # Rendre le template avec les résultats
            return redirect('/afficher_resultat')
        except Exception as e:
            return {"error": f"Erreur lors de l'appel à l'API : {str(e)}"}
        
        
api.add_resource(AfficherDecisionApprobationResource, '/afficher_decision_approbation')
        
        
if __name__ == '__main__':
    app.run(debug=True, port=5009)