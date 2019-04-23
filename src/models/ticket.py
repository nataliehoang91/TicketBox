from src import db

class Ticket(db.model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    ticket_type_id
    order_id=
    used=db.Column(db.Boolean)
    position=db.Column(db.String)