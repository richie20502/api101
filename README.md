# Nombre del Proyecto

Descripción breve del proyecto: qué hace, por qué es útil y a quién está dirigido.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Instalación

Instrucciones para instalar y configurar el proyecto. Asegúrate de incluir cualquier requisito previo.

### Requisitos previos

Lista de las dependencias que deben instalarse antes de usar el proyecto.

```bash
#instalar virtual env
pip install virtualenv

#Generar virtual env
virtualenv venv

#activar virtual env
venv\Scripts\activate

# Ejemplo para Python
pip install -r requirements.txt

#agregamos el modo debug

FLASK_ENV=development flask run

#MVC ORM

pip install Flask SQLAlchemy

```

### Estructura del proyecto

```bash
├── app.py                   # Archivo principal que arranca la aplicación
├── config.py                # Configuración de la aplicación (incluye la conexión a la base de datos)
├── models/                  # Directorio de modelos (SQLAlchemy)
│   ├── __init__.py          # Inicializador de los modelos y conexión a la DB
│   └── usuario.py           # Modelo de la tabla 'usuarios'
├── controllers/             # Directorio de controladores
│   ├── __init__.py          # Inicializador del módulo de controladores
│   └── usuarios_controller.py # Controlador con la lógica de los usuarios
├── routes/                  # Directorio de rutas
│   ├── __init__.py          # Inicializador del módulo de rutas
│   └── usuarios.py          # Rutas de usuarios
├── db.py                    # Archivo para inicializar la base de datos
└── requirements.txt         # Dependencias del proyecto

```
