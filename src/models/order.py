from src import db

class Order(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    tickets=db.relationship('Ticket', backref='order', lazy=True)
    status=db.Column(db.String,nullable=False)