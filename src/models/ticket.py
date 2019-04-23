from src import db

class Ticket(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    ticket_type_id=db.Column(db.Integer, db.ForeignKey('tickettype.id'),
        nullable=False)
    order_id=db.Column(db.Integer, db.ForeignKey('order.id'),
        nullable=False)
    used=db.Column(db.Boolean)
    position=db.Column(db.String)