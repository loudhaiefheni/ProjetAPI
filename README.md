# ProjetAPI

## Prérequis

Assurez-vous d'avoir les éléments suivants installés avant d'exécuter le code :

- Python 3.x
- Flask (`pip install Flask`)
- Flask-RESTful (`pip install flask-restful`)

## Description du projet

Ce projet consiste en une migration d'une application utilisant des services SOAP vers une application Flask utilisant des API RESTful. L'objectif est d'automatiser le processus de prêt bancaire en évaluant la solvabilité des clients, en évaluant leurs propriétés, en calculant leur score de crédit et en prenant des décisions d'approbation.

## Composants du projet

1. **extractionAPI.py**

   Ce composant permet l'extraction des données client à partir d'un fichier texte `demande_client.txt`. Il extrait les données, les stocke dans un fichier JSON `client_info.json`, et attribue un identifiant unique à chaque ensemble de données client.

2. **solvabiliteAPI.py**

   Ce service évalue la solvabilité du client en fonction des données contenues dans `client_info.json`. Il attribue la valeur "Solvable" ou "Non Solvable" pour chaque client en fonction de certains critères.

3. **evaluationAPI.py**

   Ce service évalue la propriété des clients en fonction des données contenues dans `client_info.json`. Il attribue la valeur "Bien évalué" ou "Mal évalué" pour chaque client en fonction de certains critères.

4. **credit_scoreAPI.py**

   Ce service calcule le score de crédit de chaque client en fonction des données de solvabilité et d'évaluation de propriété. Les scores de crédit sont stockés dans `client_info.json`.

5. **approbationAPI.py**

   Ce service prend des décisions d'approbation en fonction des scores de crédit, de la solvabilité et de l'évaluation de propriété. Il attribue une décision "Positif" ou "Négatif" pour chaque client en fonction de certains critères. Les décisions d'approbation sont stockées dans `client_info.json`.

6. **compositeAPI.py**

   Ce composant permet à un utilisateur d'entrer des informations client via une interface utilisateur Tkinter. Il appelle ensuite les autres services de manière séquentielle pour effectuer le scoring de crédit complet et affiche la décision d'approbation.

## Utilisation des API

Chaque API expose des ressources RESTful qui peuvent être appelées via des requêtes HTTP. Voici les ressources disponibles pour chaque API :

- **extractionAPI.py**
  - Ressource : `/extract_client_data`

- **solvabiliteAPI.py**
  - Ressource : `/check_solvency`

- **evaluationAPI.py**
  - Ressource : `/evaluate_property`

- **credit_scoreAPI.py**
  - Ressource : `/calculate_credit_score`

- **approbationAPI.py**
  - Ressource : `/take_approval_decision`

- **compositeAPI.py**
  - Ressource : `/composite_service_workflow`

⚠️ **Attention :** Assurez-vous d'exécuter chaque API et d'utiliser des clients HTTP appropriés pour appeler les ressources correspondantes.

## Exécution du code
1. Clônez ce dépôt sur votre machine locale :

```bash
git clone https://url.du.depot.git
```
2. Accédez au répertoire du projet :

```bash
cd chemin/vers/le/projet
```
⚠️ **Attention :** Assurez-vous que tous les fichiers requis sont présents, notamment `app.py`, `compositeAPI.py`, `extractionAPI.py` , `credit_scoreAPI.py`, `solvabiliteAPI.py`, `evaluationAPI.py`, `approbationAPI.py` et `client_info.json`.

3. Activez l'environnement virtuel : 
```bash
source Venv/bin/activate
```
4. Lancez l'application Flask :

```bash
python app.py
```
⚠️ **Attention :** Assurez-vous de spécifier un port disponible si le `port 5000` est déjà utilisé.

5. Ouvrez votre navigateur Web et accédez à l'adresse suivante : `http://localhost:5000`

    - Vous serez redirigé vers la page de connexion.

6. Utilisez les identifiants suivants pour vous connecter :

    - Nom d'utilisateur : `admin`
    - Mot de passe : `admin`

✔️ **Complété** Une fois connecté, vous pourrez utiliser l'application.

📝 **Note :** afin de faciliter la saisie de la demande, voici un exemple à copier et à coller dans le formulaire : 

        Nom du client:Houssem Halweni
        Adresse:Rue
        Email:stephaneloiseaux@gmail.com 
        Telephone:075566
        Montant pret demandees:4000EUR 
        Duree de pret:ans 
        Revenu Mensuel:10EUR
        Depence Mensuelle:50EUR
        indicateur gaz et electricite:C
