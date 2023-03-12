from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField
from wtforms.validators import InputRequired
from baiter.models import classes


class VictimForm(FlaskForm):
    name = StringField('Name')
    server = StringField('Server')
    wow_class = SelectField(
        'Class',
        validators=[InputRequired()],
        choices=[(c.css, c.pretty_name) for c in classes]
    )
    x_coord = FloatField('X Coordinate')
    y_coord = FloatField('Y Coordinate')
