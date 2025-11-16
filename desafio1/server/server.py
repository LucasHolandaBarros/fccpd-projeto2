from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Olá! Servidor Flask funcionando dentro do container 🎉"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)