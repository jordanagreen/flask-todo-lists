from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Jordan'}  # fake user
    lists = [
        {'author': {'name': 'Jordan'},
         'title': 'Shopping List',
         'items': ['Eggs', 'Milk'],
         'ordered': False
         },
        {'author': {'name': 'Jordan'},
         'title': 'Schedule',
         'items': ['Eat', 'Sleep'],
         'ordered': True
         }
        ]

    return render_template('index.html',
                           title='Home',
                           user=user,
                           lists=lists)
