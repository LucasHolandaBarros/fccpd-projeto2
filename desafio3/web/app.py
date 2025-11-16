from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

# Redis
redis_host = os.getenv("REDIS_HOST", "cache")
r = redis.Redis(host=redis_host, port=6379)

# Postgres
db_host = os.getenv("DB_HOST", "db")
conn = psycopg2.connect(
    dbname="mydb",
    user="myuser",
    password="mypassword",
    host=db_host
)

@app.route("/")
def index():
    # Teste Redis
    r.incr("visitas")
    visitas = r.get("visitas").decode()

    # Teste DB
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM produtos;")
    count = cur.fetchone()[0]

    return {
        "status": "ok",
        "visitas_redis": visitas,
        "produtos_no_db": count
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
