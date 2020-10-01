from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    myChoices = [(1, 'Research Proposals and Theses'), (2, 'Linguistics'),
                 (3, 'Undergraduate Studies'), (4, 'General')]
    category = SelectField('Category', coerce=int,
                           choices=myChoices, validators=[DataRequired()])
    submit = SubmitField('Post')
