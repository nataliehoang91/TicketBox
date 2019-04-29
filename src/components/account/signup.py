from flask import Blueprint, render_template,request
from src import db
from datetime import datetime
# from DateTime import DateTime

from flask import Flask, render_template, flash, redirect, url_for,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager,login_user,logout_user, current_user, login_required
from flask import request
from flask import session
from sqlalchemy import desc
from werkzeug.security import generate_password_hash, check_password_hash


signup_blueprint=Blueprint('account',__name__,template_folder='../../templates')


from src.components.account.form import SignUpForm
from src.models.user import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


def set_password(password):
      password_hash = generate_password_hash(password)
@signup_blueprint.route('/signup',methods=['POST','GET'])
def add():
    form=SignUpForm()
    if request.method == 'POST':
        u=User(username=form.username.data,email=form.email.data,phonenumber="form.phonenumber.data",password_hash=generate_password_hash(form.password_hash.data))
        print("username")
        db.session.add(u)
        db.session.commit()

        print('*******', u.id)
        
    return render_template('signup.html',form=form)  



@signup_blueprint.route('/',methods=['POST','GET'])
def login():
    form=LoginForm()
    if request.method == 'POST':
        u=User(username=form.username.data,email=form.email.data,phonenumber="form.phonenumber.data",password_hash=generate_password_hash(form.password_hash.data))
       
        db.session.add(u)
        db.session.commit()

        if request.method == 'POST':
        email=request.form["email"]
        password=request.form["password"]
        user=User.query.filter_by(email=email).first()
        if user is not None and user.check_password(password):

        
    return render_template('home.html',form=form)  

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
