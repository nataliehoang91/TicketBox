from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,SubmitField,DateTimeField,SelectField,validators, TimeField, PasswordField
from wtforms.validators import EqualTo,Email,DataRequired
class SignUpForm(FlaskForm):
    username=StringField('Username: ',[validators.DataRequired(),validators.Length(min=6,max=16)])
    email=StringField("Email: ",[validators.DataRequired()])
    phonenumber=StringField("Phone Number: ")
    password_hash=StringField("Password: ",[validators.DataRequired()])
    # starttime=DateField("Time", format='%Y-%m-%d')
    submit=SubmitField('Create' )

class LoginForm(FlaskForm):
    email=StringField("Email: ",[validators.DataRequired()])
    password_hash=PasswordField("Password: ",[validators.DataRequired()])
    # starttime=DateField("Time", format='%Y-%m-%d')
    submit=SubmitField('Login' )

class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit=SubmitField('Reset' )

class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Repeat Password', validators=[
            EqualTo("password", message='Passwords must match.')
            ])
    submit=SubmitField('Submit' )