from flask import render_template, flash, redirect, request, abort, url_for, g
from app import app, login_manager
from forms import LoginForm
from models import User, TodoList
from flask_login import login_user, logout_user, login_required, current_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home',
                           user=g.user)


@app.route('/list/<id>')
@login_required
def show_list(id):
    l = TodoList.query.get(id)
    return render_template('list.html',
                           title=l.title,
                           list=l)


@app.route('/login', methods=['GET', 'POST'])
def login():
    def next_is_valid(next):
        return True
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user is None: # user doesn't exist
            flash('Invalid username.')
            return render_template('login.html',
                                   title='Sign in',
                                   form=form)
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


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.before_request
def before_request():
    g.user = current_user
