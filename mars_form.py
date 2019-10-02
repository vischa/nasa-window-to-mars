from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class DataForm(FlaskForm):
    rover = StringField('Rover Name [Select from curiorsity, spirit or opportunity]', validators=[DataRequired()])
    sol = StringField('Martian Sol [Days counting from spacecraft landing on Mars]', validators=[DataRequired()])
    camera = StringField('On-board Camera', validators=[DataRequired()])
    submit = SubmitField('Get Photos!')
