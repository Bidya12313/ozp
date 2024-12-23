from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Ім'я користувача", validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={'class': 'form-control', 'pattern': '[0-9]*', 'title': 'Тільки цифри'})
    submit = SubmitField("Увійти", render_kw={'class': 'form-control'})