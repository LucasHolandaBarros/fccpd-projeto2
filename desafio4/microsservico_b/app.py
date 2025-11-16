from flask import Flask, jsonify
import requests

app = Flask(__name__)

MICROSERVICO_A_URL = "http://microsservico_a:5000/usuarios"

@app.route("/usuarios_completos", methods=["GET"])
def usuarios_completos():
    try:
        response = requests.get(MICROSERVICO_A_URL)
        response.raise_for_status()
        usuarios = response.json()

        resultado = [
            f"Usuário {u['nome']} ativo desde {u['ativo_desde']}"
            for u in usuarios
        ]
        return jsonify(resultado)

    except requests.exceptions.RequestException as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
