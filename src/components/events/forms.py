from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,SubmitField,DateTimeField,SelectField,validators, TimeField

class AddEventForm(FlaskForm):
    title=StringField('Event Title: ',[validators.DataRequired(),validators.Length(min=4,max=25)])
    description=StringField('Description of Event: ',[validators.DataRequired(),validators.Length(min=10,max=500)])
    venue=StringField('Venue: ',[validators.DataRequired()])
    location=StringField('Location Address: ',[validators.DataRequired()])
    phonenumber=StringField('Phonenumber: ',[validators.DataRequired()])
    
    eventtype=SelectField('Type' ,coerce=int)
    eventowner=StringField("Event Organizer")
    imglink=StringField('Poster: ')
    # starttime=DateField("Time", format='%Y-%m-%d')
    submit=SubmitField('Create' )
