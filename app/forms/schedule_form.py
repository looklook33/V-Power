from flask_wtf import FlaskForm
from wtforms import StringField, TimeField
from wtforms.validators import DataRequired, Length

class ScheduleForm(FlaskForm):
    describe = StringField('Describe', validators=[Length(max=255)])
    startTime = TimeField('Start Time', validators=[DataRequired()])
    endTime = TimeField('End Time', validators=[DataRequired()])