from flask import render_template, flash, redirect
from app import app
from forms import LoginForm
from models import TodoList


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Jordan'}  # fake user
    # lists = [
    #     {'author': {'name': 'Jordan'},
    #      'title': 'Shopping List',
    #      'items': ['Eggs', 'Milk'],
    #      'ordered': False
    #      },
    #     {'author': {'name': 'Jordan'},
    #      'title': 'Schedule',
    #      'items': ['Eat', 'Sleep'],
    #      'ordered': True
    #      }
    #     ]

    lists = TodoList.query.all()

    return render_template('index.html',
                           title='Home',
                           user=user,
                           lists=lists)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login for name %s, remember=%s' %
              (form.name.data, form.remember_me.data))
        return redirect('index')
    return render_template('login.html',
                           title='Sign in',
                           form=form)