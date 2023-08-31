#importar framework para criar back end
from flask import Flask

app = Flask("meu app")
#criar pasta ou caminho do site
@app.route('/')
def hello():
     return "Olá Mundo"
#criar pasta ou caminho do site
@app.route('/novo')
def novo():
     return "<h1> Nova Página </h1>"