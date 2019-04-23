from src import db


class Tickettype(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    ticket_type=db.Column(db.String,nullable=False)
    tickets=db.relationship('Ticket', backref='tickettype', lazy=True)
    price=db.Column(db.Integer, nullable=False)
    quantity=db.Column(db.Integer,nullable=False)