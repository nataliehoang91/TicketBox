
from src import db
from flask_login import UserMixin
from flask import Flask, render_template, flash, redirect, url_for,request

import requests
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

    # def send_password_reset_email(self, token):
    #     apikey = "get-this-from-mailgun"
    #     domain_name = "get-this-from-mailgun"
    #     print(render_template('email.html', token=token))
    #     requests.post(
    #         "https://api.mailgun.net/v3/" + domain_name + "/messages",
    #         auth=("api", apikey),
    #         data={"from": "ticketbox.mt@" + domain_name,
    #               "to": [self.email],
    #               "subject": "Reset password",
    #               "html": render_template('email.html', token=token)})




    def send_password_reset_email(self, token):
        apikey = "hide"
        url = "hide"

        requests.post(url, 
            auth=("api", apikey), 
            data={"from": "hide",
            "to": [self.email], 
            "subject": "Reset Password", 
            "html":render_template('email.html', token=token)}
)