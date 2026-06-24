from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a la aplicación de deportes extremos"

@app.route('/api/data', methods=['GET'])
def get_data():
    # Aquí puedes agregar la lógica para manejar las peticiones y devolver datos
    data = {
        "mensaje": "Datos de deportes extremos"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)