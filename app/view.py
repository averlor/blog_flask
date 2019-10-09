from flask import render_template

from app import app


@app.route('/')
def index():
    name = 'Vasya'
    return render_template('index.html', payload=name)
