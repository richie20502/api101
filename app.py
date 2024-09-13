from flask import Flask, request, jsonify;

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message" : "Bienvendo api flask dsm 101"
    })

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
    app.run(debug=False)