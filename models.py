from app import db
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    lists = db.relationship('TodoList', backref='author', lazy='dynamic')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % self.name


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    is_ordered = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    items = db.relationship('ListItem', backref='list', lazy='dynamic')

    def __repr__(self):
        return '<List %r>' % self.title


class ListItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    list_id = db.Column(db.Integer, db.ForeignKey('todo_list.id'))

    def __repr__(self):
        return '<Item %r>' % self.text

