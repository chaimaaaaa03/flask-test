# app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Bienvenue sur mon API Flask !"})

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello depuis Flask !"})

if __name__ == "__main__":
    app.run(debug=True)
