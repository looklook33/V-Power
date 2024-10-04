from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField
from wtforms.validators import Length

class RoleForm(FlaskForm):
    isMember = BooleanField('Is Member')
    isTrainer = BooleanField('Is Trainer')
    isManager = BooleanField('Is Manager')
    discribe = StringField('Discribe', validators=[Length(max=255)])