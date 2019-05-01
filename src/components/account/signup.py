from flask import Blueprint, render_template,request
from src import db
from datetime import datetime
# from DateTime import DateTime

from flask import Flask, render_template, flash, redirect, url_for,request

from flask_login import UserMixin, LoginManager,login_user,logout_user, current_user, login_required
from flask import request
from flask import session

from werkzeug.security import generate_password_hash, check_password_hash


signup_blueprint=Blueprint('account',__name__,template_folder='../../templates')


from src.components.account.form import SignUpForm, LoginForm
from src.models.user import User


# def set_password(password):
#       password_hash = generate_password_hash(password)

# def check_password(self, password):
#       return check_password_hash(password_hash, password)


@signup_blueprint.route('/signup',methods=['POST','GET'])
def add():
    form=SignUpForm()
    if request.method == 'POST':
        u=User(username=form.username.data,email=form.email.data,phonenumber="form.phonenumber.data",password_hash=generate_password_hash(form.password_hash.data))
        print("username")
        db.session.add(u)
        db.session.commit()
        flash("Your account has been successfully created")
        print('*******', u.id)
        return redirect('/')
    return render_template('signup.html',form=form)  



@signup_blueprint.route('/',methods=['POST','GET'])
def login():
    form=LoginForm()
    if request.method == 'POST':
        email=form.email.data
        password=form.password_hash.data
        user=User.query.filter_by(email=email).first()
        if user is not None and check_password_hash(user.password_hash,password):
            login_user(user)
            session['username'] = user.username
            
 #user here being the user object you have queried
            print(user.username)
    return render_template('home.html', form=form)


@signup_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    del session['username']
    return redirect('/')

        
     


