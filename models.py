from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    lists = db.relationship('TodoList', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.name


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    timestamp = db.Column(db.DateTime)
    is_ordered = db.column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    items = db.relationship('ListItem', backref='list', lazy='dynamic')

    def __repr__(self):
        return '<List %r>' % self.title


class ListItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime)
    list_id = db.Column(db.Integer, db.ForeignKey('todo_list.id'))

    def __repr__(self):
        return '<Item %r>' % self.text

