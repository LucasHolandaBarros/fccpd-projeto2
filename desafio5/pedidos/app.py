from flask import Flask, jsonify

app = Flask(__name__)

PEDIDOS = [
    {"id": 1, "user_id": 1, "product": "Notebook"},
    {"id": 2, "user_id": 2, "product": "Celular"},
]

@app.route("/pedidos", methods=["GET"])
def get_pedidos():
    return jsonify(PEDIDOS), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
