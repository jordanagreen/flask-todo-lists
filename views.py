from flask import render_template, flash, redirect, request, abort, url_for
from app import app, login_manager
from forms import LoginForm
from models import User, TodoList
from flask_login import login_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Jordan'}  # fake user
    lists = TodoList.query.all()
    return render_template('index.html',
                           title='Home',
                           user=user,
                           lists=lists)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        login_user(user, remember=form.remember_me.data)
        flash('Login for name %s, remember=%s' %
              (form.name.data, form.remember_me.data))
        next = request.args.get('next')
        if not next_is_valid(next):
            return abort(400)
        return redirect(next or url_for('index'))
    return render_template('login.html',
                           title='Sign in',
                           form=form)


def next_is_valid(next):
    return True
