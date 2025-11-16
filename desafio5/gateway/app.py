from flask import Flask, jsonify
import requests

app = Flask(__name__)

USERS_SERVICE_URL = "http://usuarios:5001/usuarios"
ORDERS_SERVICE_URL = "http://pedidos:5002/pedidos"

@app.route("/users", methods=["GET"])
def users():
    resp = requests.get(USERS_SERVICE_URL)
    return jsonify(resp.json()), resp.status_code

@app.route("/orders", methods=["GET"])
def orders():
    resp = requests.get(ORDERS_SERVICE_URL)
    return jsonify(resp.json()), resp.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
