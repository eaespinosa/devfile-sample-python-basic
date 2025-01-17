from flask import Flask, render_template, request, url_for, flash, redirect
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/create')
def create():
    return render_template("create.html")


if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
