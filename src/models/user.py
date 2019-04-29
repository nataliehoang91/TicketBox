
from src import db
from flask_login import UserMixin

class User(UserMixin,db.Model):

  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key=True)
  username=db.Column(db.String(80),index=True, unique=True)
  password_hash = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(120), index=True, unique=True)
  phonenumber=db.Column(db.String(80))
  events = db.relationship('Event', backref='user', lazy=True)
  tickets=db.relationship('Ticket',backref='user', lazy=True)
  orders=db.relationship('Order',backref='user', lazy=True)
  

  def set_password(self, password):
      self.password_hash = generate_password_hash(password)

  def check_password(self, password):
      return check_password_hash(self.password_hash, password)

  # password hash is kept in database

    