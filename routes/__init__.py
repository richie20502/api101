from routes.usuarios import usuarios_routes

def init_routes(app):
    app.register_blueprint(usuarios_routes)