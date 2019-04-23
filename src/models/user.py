
from src import db

class User(db.Model):

  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128), nullable=False)
  events = db.relationship('Event', backref='user', lazy=True)
  tickets=db.relationship('Ticket',backref='user', lazy=True)
  orders=db.relationship('Order',backref='user', lazy=True)



# class Venue(db.model):
#     id
#     venue_name
#     location

# class TicketTypes(db.model):
#     id
#     ticket_type
#     event_id
#     expire_at
#     price
#     quota

# class Ticket(db.model):
#     id
#     user_id
#     ticket_type_id
#     order_id
#     used 
#     position 

# class Orders(db.model):
#     id 
#     user_id
#     status 
    