from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,SubmitField,DateTimeField,SelectField,validators, TimeField

class AddEventForm(FlaskForm):
    title=StringField('Event Title: ',[validators.DataRequired(),validators.Length(min=4,max=25)])
    description=StringField('Description of Event: ',[validators.DataRequired(),validators.Length(min=10,max=500)])
    venue=StringField('Venue: ',[validators.DataRequired()])
    location=StringField('Location Address: ',[validators.DataRequired()])
    email=StringField("Email: ",[validators.DataRequired()])
    name=StringField("Name: ",[validators.DataRequired()])
    phonenumber=StringField("Phone Number: ",[validators.DataRequired()])
    eventtype=SelectField('Type' ,coerce=int)
    # starttime=DateField("Time", format='%Y-%m-%d')
    submit=SubmitField('Create' )
