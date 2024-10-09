from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'aditya'}
    posts = [
        {
            'author' : {'username' : 'ashish'},
            'body': 'i played mini militia!'
        },
        {
            'author': {'username':'om'},
            'body': 'founder, thedesigncompany'
        },
        {
            'author': {'username':'shravani'},
            'body': 'nothing, just trying the app'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)