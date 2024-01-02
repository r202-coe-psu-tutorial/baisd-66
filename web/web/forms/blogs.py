from flask_wtf import FlaskForm
from wtforms import fields, validators


class MessageForm(FlaskForm):
    message = fields.StringField(
        "Message", validators=[validators.DataRequired(), validators.Length(min=3)]
    )


class GroupForm(FlaskForm):
    name = fields.StringField(
        "Name", validators=[validators.DataRequired(), validators.Length(min=3)]
    )


class LoginForm(FlaskForm):
    username = fields.StringField(
        "Username", validators=[validators.DataRequired(), validators.Length(min=3)]
    )
    password = fields.PasswordField(
        "Password", validators=[validators.DataRequired(), validators.Length(min=3)]
    )


class RegistrationForm(FlaskForm):
    username = fields.StringField(
        "Username", validators=[validators.DataRequired(), validators.Length(min=3)]
    )
    email = fields.StringField(
        "Email",
        validators=[
            validators.DataRequired(),
            validators.Length(min=3),
            validators.Email(),
        ],
    )
    password = fields.PasswordField(
        "Password", validators=[validators.DataRequired(), validators.Length(min=3)]
    )
    password_confirm = fields.PasswordField(
        "Password Confirm",
        validators=[
            validators.DataRequired(),
            validators.Length(min=3),
            validators.EqualTo("password", message="Passwords must match"),
        ],
    )
