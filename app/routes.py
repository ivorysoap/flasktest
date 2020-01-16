# All of our pages

from flask import render_template, flash, redirect
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

@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('about'))
    return render_template('login.html', title='Sign In', form=form)