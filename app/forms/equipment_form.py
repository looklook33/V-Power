from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class EquipmentForm(FlaskForm):
    type = StringField('Type', validators=[DataRequired(), Length(max=100)])
    url = StringField('URL', validators=[Length(max=255)])
    describe = StringField('Describe', validators=[Length(max=255)])