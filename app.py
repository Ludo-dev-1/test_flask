from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    # envoie une réponse 'Hello World!' au client
    return 'Hello, World!'

@app.route('/data')
def data():
    return jsonify({'name': 'Pikachu', 'power': 20, 'life': 50})

@app.route('/car')
def car():
    return jsonify({'name': 'Peugeot3008', 'power': 110, 'color': 'Grey'},{'name': 'Renault_Clio', 'power': 70, 'color': 'Yellow'},{'name': 'Golf', 'power': 150, 'color': 'Red'})