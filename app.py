from flask import Flask, request, jsonify;
import pymysql

app = Flask(__name__)

def get_db_connection():
    connection =  pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='101',
        cursorclass=pymysql.cursors.DictCursor)
    return connection

@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    print("holah-------------hhh")
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql ="SELECT id, nombre, email FROM usuarios"
        cursor.execute(sql)
        usuarios = cursor.fetchall()
    connection.close()
    return jsonify(usuarios)


@app.route('/api/usuarios', methods=['POST'])
def add_usuarios():
    data = request.json
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
        cursor.execute(sql,(data['nombre'], data['email']))
        connection.commit()
    connection.close()
    return jsonify({ "message" : "Usuario agregado correctamente"}), 201
    
        

@app.route('/')
def home():
    return jsonify({
        "message" : "Bienvendo api flask dsm 101"
    })
    
@app.route('/api/data', methods=['GET'])
def det_data_get():
    content_body = {
        "name": "Ricardo",
        "last_name": "Lugo"
    }
    return jsonify(content_body)

@app.route('/api/data', methods=['POST'])
def det_data_post():
    content_body = request.json
    print("******************")
    print(content_body)
    print("******************")
    return jsonify({
        "recived" : content_body
    })


if __name__ == '__main__':
    app.run(debug=True)