
from src import db

class User(db.Model):

  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key=True)
  username=db.Column(db.String(80),index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  phonenumber=db.Column(db.String(80),nullable=True)
  events = db.relationship('Event', backref='user', lazy=True)
  tickets=db.relationship('Ticket',backref='user', lazy=True)
  orders=db.relationship('Order',backref='user', lazy=True)
  # password hash is kept in database

    