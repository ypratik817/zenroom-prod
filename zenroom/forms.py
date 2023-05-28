from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,SelectField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo
from wtforms.widgets import TextArea


class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=3, max=200)])
    password = PasswordField('Password',
                           validators=[DataRequired(), Length(min=3, max=400)])
    submit = SubmitField('Submit')
    regi_email = StringField('Email', validators=[DataRequired(), Length(min=3, max=200)])
    regi_password = PasswordField("Password",validators=[DataRequired(), Length(min=8, max=400) , EqualTo("regi_confirm_password", message='Passwords must match')])
    regi_confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=8, max=400), EqualTo("regi_password", message='Passwords must match')])
    regi_gender = SelectField('Gender', choices=[('male','Male'),('female','Female'),('other','Other')])
    age = IntegerField('Age',validators=[DataRequired()] )
    def validate(self):
        if not super().validate():
            return False
        if self.password.data != self.confirm_password.data:
            raise ValidationError('Passwords do not match.')

class Diary(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=200)])
    note = StringField('Note',
                           validators=[DataRequired(), Length(min=3, max=2000)], widget=TextArea())
    submit = SubmitField('Submit')

class Diet(FlaskForm):
    age = IntegerField("Age",validators=[DataRequired(), Length(max=4)])
    gender=SelectField("Gender",choices=[('male','Male'),('female','Female'),('other','Other')])
    diseases=StringField("Diseases",validators=[Length(min=3,max=200)])
    calories=IntegerField("Calories",validators=[Length(max=4)])
    submit = SubmitField('Submit')