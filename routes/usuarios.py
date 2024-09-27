from flask import Blueprint, request, jsonify
from controllers.usuarios_controller import obtener_usuarios, agregar_usuario  # Importar correctamente las funciones

usuarios_routes = Blueprint('usuarios', __name__)

@usuarios_routes.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = obtener_usuarios()
    return jsonify(usuarios)

@usuarios_routes.route('/api/usuarios', methods=['POST'])
def post_usuario():
    data = request.json
    mensaje = agregar_usuario(data['nombre'], data['email'])
    return jsonify({"message": mensaje}), 201
