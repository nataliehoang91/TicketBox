from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,SubmitField,DateTimeField,SelectField,validators, TimeField

class SignUpForm(FlaskForm):
    username=StringField('Username: ',[validators.DataRequired(),validators.Length(min=6,max=16)])
    email=StringField("Email: ",[validators.DataRequired()])
    phonenumber=StringField("Phone Number: ")
    password_hash=StringField("Password: ",[validators.DataRequired()])
    # starttime=DateField("Time", format='%Y-%m-%d')
    submit=SubmitField('Create' )

class LoginForm(FlaskForm):
    email=StringField("Email: ",[validators.DataRequired()])
    password_hash=StringField("Password: ",[validators.DataRequired()])
    # starttime=DateField("Time", format='%Y-%m-%d')
    submit=SubmitField('Login' )
