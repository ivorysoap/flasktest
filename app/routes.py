# All of our pages

from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/about')

def about():
    user = {'username' : 'Ivor'}
    posts = [

        {
            'author' : { 'username' : 'Simon' },
            'body'   : 'Cybersecurity is cool'
        },
        {
            'author' : { 'username' : 'Akinyele' },
            'body'   : 'Ruby is cool'
        }

    ]
    return render_template('title.html', title='Home', user=user, posts=posts)

@app.route('/login')

def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)