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

```

### Estructura del proyecto

```bash
├── app.py                     # Archivo principal que arranca la aplicación
├── controllers/
│   ├── __init__.py            # Inicializador del módulo
│   └── usuarios_controller.py # Lógica para usuarios
├── routes/
│   ├── __init__.py            # Inicializador del módulo, y registro de rutas
│   └── usuarios.py            # Rutas de usuarios que llaman a los controladores
├── db.py                      # Archivo para la conexión a la base de datos
└── requirements.txt           # Dependencias del proyecto

```
