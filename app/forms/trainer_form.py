from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class TrainerForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    lastName = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    username = StringField('Username', validators=[DataRequired(), Length(max=50)])
    hashedPassword = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    specialty = StringField('Specialty', validators=[Length(max=100)])