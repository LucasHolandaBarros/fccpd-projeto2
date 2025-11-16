from flask import Flask, jsonify

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Lucas", "ativo_desde": "2021-05-01"},
    {"id": 2, "nome": "Maria", "ativo_desde": "2022-03-15"},
    {"id": 3, "nome": "João", "ativo_desde": "2020-11-20"}
]

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
