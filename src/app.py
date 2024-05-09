"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planetas
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def cargar_usuarios():

    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))

    return jsonify(all_users), 200

@app.route('/planets', methods=['GET'])
def cargar_planetas():

    planetas = Planetas.query.all()
    all_planetas = list(map(lambda x: x.serialize(), planetas))

    return jsonify(all_planetas), 200

@app.route('/user/<int:usuario_id>', methods=['GET'])
def cargar_usuario(usuario_id):

    user = User.query.get(usuario_id)

    if user is None:
        raise APIException("Usuario no encontrado", status_code=404)
    
    user_data = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "password": user.password
    }

    return jsonify(user_data), 200

@app.route('/user', methods=['POST'])
def crear_usuario():    
    body = request.get_json()
    user= User(name=body['name'], email=body['email'], password=body['password'])
    db.session.add(user)
    db.session.commit()
    response_body = {
        "msg": "Usuario creado "
    }
    return jsonify(response_body), 200

@app.route('/user/<int:usuario_id>', methods=['PUT'])
def editar_usuario(usuario_id):
    # Obtener el cuerpo de la solicitud en formato JSON
    body = request.get_json()

    # Obtener el usuario por ID
    user = User.query.get(usuario_id)

    # Verificar si el usuario existe
    if user is None:
        raise APIException("Usuario no encontrado", status_code=404)
    
    # Actualizar los campos del usuario si se proporcionan en el cuerpo de la solicitud
    if body is not None:
        if "name" in body:
            user.name = body["name"]
        if "email" in body:
            user.email = body["email"]
        
        # Commit para guardar los cambios en la base de datos
        db.session.commit()

        # Crear una respuesta exitosa
        response_body = {
            "msg": "Usuario editado exitosamente",
            "id": user.id,
            "name": user.name,
            "email": user.email
            # Puedes agregar más campos aquí si lo deseas
        }
        return jsonify(response_body), 200
    else:
        # Si no se proporcionaron datos en el cuerpo de la solicitud
        raise APIException("No se proporcionaron datos para editar el usuario", status_code=400)


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
