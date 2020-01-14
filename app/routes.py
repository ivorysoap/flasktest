# All of our pages

from flask import render_template
from app import app

@app.route('/')
@app.route('/about')

def index():
    user = {'username' : 'Ivor'}
    return render_template('title.html', title='Home', user=user)
