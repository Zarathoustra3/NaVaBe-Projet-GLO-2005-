from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Bonjour, Ceci est un test du module flask"