import json

import requests
from flask import Flask, render_template, json

app = Flask(__name__)
origine = requests.get('https://poetrydb.org/author,title/Shakespeare;Sonnet')
dati = json.loads(origine.content)

@app.route("/")
def index():
    return render_template('index.html', poesia = dati[2])


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

