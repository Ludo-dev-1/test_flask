# 🚗 test_flask

Petit projet Flask basé sur le projet de démonstration **flask-demo**, avec l'ajout d'une nouvelle route API.

## 📌 Description

`test_flask` est une application web simple développée avec **Flask**.  
Elle reprend les routes existantes du projet `flask-demo` et ajoute une nouvelle route permettant de récupérer une liste de voitures au format JSON.

## ⚙️ Installation

1. Cloner le projet :
```bash
git clone <url-du-repo>
cd test_flask
```

## Créer un environnement virtuel (optionnel mais recommandé) :

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
# ou
venv\Scripts\activate     # Window
```
## Installer les dépendances :

```bash
pip install flas
```
## Lancement du projet :

```bash
python app.py
```

## Puis ouvrir dans le navigateur :

http://127.0.0.1:5000/

## Routes disponibles :

 -  / :
Retourne hello word! 

- /data : Retourne un json de pokemon 

- /car : Retourne une liste d'objet en json de voitures