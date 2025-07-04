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
        choices=[(c, v['pretty_name']) for c, v in classes.items()]
    )
    x_coord = FloatField('X Coordinate')
    y_coord = FloatField('Y Coordinate')
