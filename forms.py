from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Optional, URL


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField(
        'Username',
        validators=[DataRequired()],
    )

    email = StringField(
        'E-mail',
        validators=[DataRequired(), Email()],
    )

    password = PasswordField(
        'Password',
        validators=[Length(min=6)],
    )
    image_url = StringField(
        '(Optional) Image URL',
        validators = [Optional(),
                      URL()]
    )


class UserEditForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired()],
    )

    email = StringField(
        'E-mail',
        validators=[DataRequired(), Email()],
    )

    image_url = StringField(
        '(Optional) Image URL',
        validators = [Optional(),
                      URL()]
    )

    header_image_url = StringField(
        '(Optional) Image URL',
        validators = [Optional(),
                      URL()]
    )

    bio = TextAreaField(
        'Bio',
        validators = [Optional()]
    )

    password = PasswordField(
        'Password',
        validators=[Length(min=6)],
    )


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField(
        'Username',
        validators=[DataRequired()],
    )

    password = PasswordField(
        'Password',
        validators=[Length(min=6)],
    )


class CsrfForm(FlaskForm):
    """CSRF protection form."""

