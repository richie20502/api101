swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API Flask DSM 101",
        "description": "Documentación de la API de usuarios y sus operaciones CRUD.",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": ["http"],
    "paths": {
        "/api/usuarios": {
            "get": {
                "summary": "Obtener lista de usuarios",
                "description": "Devuelve una lista de todos los usuarios registrados.",
                "responses": {
                    "200": {
                        "description": "Lista de usuarios",
                        "schema": {
                            "type": "array",
                            "items": {
                                "properties": {
                                    "id": {"type": "integer"},
                                    "nombre": {"type": "string"},
                                    "email": {"type": "string"}
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "summary": "Agregar un nuevo usuario",
                "description": "Agrega un usuario con los campos 'nombre' y 'email'.",
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "schema": {
                            "properties": {
                                "nombre": {"type": "string"},
                                "email": {"type": "string"}
                            }
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Usuario agregado correctamente"
                    }
                }
            }
        },
        "/api/usuarios/{id}": {
            "put": {
                "summary": "Actualizar un usuario",
                "description": "Actualiza un usuario proporcionando su ID.",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "type": "integer",
                        "required": True,
                        "description": "ID del usuario a actualizar"
                    },
                    {
                        "name": "body",
                        "in": "body",
                        "schema": {
                            "properties": {
                                "nombre": {"type": "string"},
                                "email": {"type": "string"}
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {"description": "Usuario actualizado correctamente"},
                    "404": {"description": "Usuario no encontrado"}
                }
            },
            "delete": {
                "summary": "Eliminar un usuario",
                "description": "Elimina un usuario proporcionando su ID.",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "type": "integer",
                        "required": True,
                        "description": "ID del usuario a eliminar"
                    }
                ],
                "responses": {
                    "200": {"description": "Usuario eliminado correctamente"},
                    "404": {"description": "Usuario no encontrado"}
                }
            }
        }
    }
}
