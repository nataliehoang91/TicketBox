from flask import Blueprint, render_template,request
from src import db
from src import app
from datetime import datetime
# from DateTime import DateTime

from flask import Flask, render_template, flash, redirect, url_for,request

from flask_login import UserMixin, LoginManager,login_user,logout_user, current_user, login_required
from flask import session
import requests
import os
from itsdangerous import URLSafeTimedSerializer

from werkzeug.security import generate_password_hash, check_password_hash


signup_blueprint=Blueprint('account',__name__,template_folder='../../templates')


from src.components.account.form import SignUpForm, LoginForm,EmailForm,PasswordForm
from src.models.user import User
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

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
        
@signup_blueprint.route('/send', methods=["GET", "POST"])
def send_password_reset_email():
    apikey = "5b9ac3714f9b23cd90691c9876526349-7bce17e5-1e3cba9b"
    url = "https://api.mailgun.net/v3/sandbox3f549896228d4bdf924a4cae2d159bf0.mailgun.org/messages"

    requests.post(url, 
        auth=("api", apikey), 
        data={"from": "postmaster@sandbox3f549896228d4bdf924a4cae2d159bf0.mailgun.org",
            "to": ["natalie.hoang91@gmail.com"], 
            "subject": "Reset Password", 
            "text":"This would be where your password reset will go."}
)
     
    return render_template('home.html')
        
@signup_blueprint.route('/reset', methods=["GET", "POST"])
def reset():
    emailform = EmailForm()
    if request.method == 'POST' and emailform.validate_on_submit():
        user_email = request.form['email']
        user = User.query.filter_by(email=user_email).first_or_404()
        if user is not None:
            token = ts.dumps(user.email, salt='recover-password-secret-10794')
            user.send_password_reset_email(token)
    return render_template('reset.html', form=emailform)


@signup_blueprint.route('/new_password/<token>', methods=['GET', 'POST'])
def new_password(token):
    form = PasswordForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            email = ts.loads(token, salt='recover-password-secret-10794', max_age=3600)
        except:
            flash('The password reset link is invalid or has expired.', 'error')
            return redirect(url_for('/.signin'))
        user_password = request.form['password']
        user = User.query.filter_by(email=email).first_or_404()
        if user is not None:
            user.password_hash=generate_password_hash(user_password)
            db.session.commit()
            return redirect('/')
    return render_template('new_password.html', form=form)





#  def reset():
#     form = EmailForm()
#     if form.validate_on_submit():
#       user = User.query.filter_by(email=form.email.data).first_or_404()
#       # Redirect to the main login form here with a "password reset email sent!"
#     return render_template('reset.html', form=form)
# def reset():
#     form = EmailForm()
#     if form.validate_on_submit():
#         try:
#             user = User.query.filter_by(email=form.email.data).first_or_404()
#         except:
#             flash('Invalid email address!', 'error')
#             return render_template('password_reset_email.html', form=form)
         
#         if user.email_confirmed:
#             send_password_reset_email(user.email)
#             flash('Please check your email for a password reset link.', 'success')
#         else:
#             flash('Your email address must be confirmed before attempting a password reset.', 'error')
#         return redirect(url_for('users.login'))
 
#     return render_template('password_reset_email.html', form=form)
#@events_blueprint.route('/reset', methods=['GET', 'POST'])