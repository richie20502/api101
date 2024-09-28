from flask import Blueprint, request, jsonify

from controllers.usuarios_controller import obtener_usuario

usuarios_routes = Blueprint('usuarios',__name__)

@usuarios_routes.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = obtener_usuario()
    return jsonify(usuarios)

