from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    email = EmailField("邮箱", validators=[DataRequired(), Email()])
    password = PasswordField("密码", validators=[DataRequired()])
    submit = SubmitField('登 录')

class RegisterForm(FlaskForm):
    email = EmailField(
        "邮箱", validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    password = PasswordField(
        "密码", validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        "确认密码",
        validators=[
            DataRequired(),
            EqualTo("password", message="再次输入密码"),
        ],
    )
    submit = SubmitField('注册')
