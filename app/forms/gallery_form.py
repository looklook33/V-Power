from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class GalleryForm(FlaskForm):
    type = StringField('Type', validators=[DataRequired(), Length(max=50)])
    url = StringField('URL', validators=[DataRequired(), Length(max=255)])
    describe = StringField('Description', validators=[Length(max=255)])