from src import db


class TicketTypes(db.model):
    id=db.Column(db.Integer, primary_key=True)
    ticket_type
    event_id
    expire_at
    price
    quota