from flask import request, g
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import FeedbackPost

class FeedbackForm(FlaskForm):
    cohort = SelectField(u'Cohort', coerce=str, choices=[('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')], validators=[DataRequired()])
    track = SelectMultipleField(u'Track', coerce=str, choices=[('pd', 'Product Design'), ('gr', 'Growth'), ('bd', 'Sales & Growth')], validators=[DataRequired()])
    curriculumGrade = SelectField(u'Curriculum', choices=[('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')], validators=[DataRequired()])
    curriculumComment = StringField(u'Curriculum Comment', validators=[DataRequired()])
    projectGrade = SelectField(u'Project', choices=[('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')], validators=[DataRequired()])
    projectComment = StringField(u'Project Comment', validators=[DataRequired()])
    carDevGrade = SelectField(u'Career Development', choices=[('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')], validators=[DataRequired()])
    carDevComment = StringField(u'Career Development Comment', validators=[DataRequired()])
    overallGrade = SelectField(u'Overall', choices=[('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')], validators=[DataRequired()])
    overallComment = StringField(u'Overall Comment', validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))