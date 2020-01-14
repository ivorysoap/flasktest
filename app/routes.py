# All of our pages

from app import app

@app.route('/')
@app.route('/about')

def index():
    return "Hello, world!"