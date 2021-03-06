from datetime import datetime

from flask_login import UserMixin
from blog import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):

    __tablename__ = "user"  # users

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    last_seen = db.Column(db.DateTime)
    #posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User({self.id}, {self.usename}, {self.email}, {self.password}, {self.image_file})'


class Post(db.Model):
    __tiblename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, unique=False, default=datetime.utcnow)
    content = db.Column(db.Text(60), nullable=False)
    image_post = db.Column(db.String(30), nullable=True, default='default.png')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'User({self.title}, {self.date_posted}, {self.image_post})'

