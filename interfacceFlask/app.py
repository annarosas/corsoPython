from flask import Flask, render_template, flash,  Response, request, redirect, url_for

app = Flask(__name__)

app.secret_key = 'olomediadfdfdf'

@app.route("/app")

def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()