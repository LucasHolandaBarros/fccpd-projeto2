from flask import Flask, jsonify

app = Flask(__name__)

USUARIOS = [
    {"id": 1, "name": "Lucas"},
    {"id": 2, "name": "Maria"},
]

@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify(USUARIOS), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
