from flask import Flask, jsonify, request
from math import floor

# Clases
from app.model.patente import Patente
from app.model.matriz import Matriz


# Servidor
app = Flask(__name__)


@app.route('/ping')
def index():
    return "pong"


# Endpoint para generar patentes  por método GET
# Recibe parametro _id tipo string
# Retorna un objeto JSON con la patente
@app.route('/patentes/<int:id>')
def get_patente(id):
    try:
        patente = Patente()
        resultado = patente.crear_patente_ser(id)

        return jsonify({"patente" : resultado})
    except Exception as ex:
        return jsonify({
        "mensaje": "ha ocurrido un error en el servidor"
        })


# Endpoint para calcular sumatoria de una matriz(r,c) en relacion a
# cordeenadas x e y, por método POST
# Recibe parametro un objeto tipo JSON con los datos r,c,z,x,y todos tipo int
# Retorna un objeto JSON con el total de la sumatorio
@app.route('/matriz', methods=['POST'])
def add_matriz():
    try:
        matriz = Matriz(request.json['r'],request.json['c'],request.json['z'])
        matriz.crear_matriz()

        total = matriz.sumar_matriz(request.json['x'],request.json['y'])

        return jsonify({"total" : total})
    except Exception as ex:
        return jsonify({"mensaje": "ha ocurrido un error en el servidor"})



if __name__ == "__main__":
    app.run()
