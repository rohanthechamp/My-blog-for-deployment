from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    Name = StringField("Name", validators=[DataRequired()])
    Email = StringField("Email", validators=[DataRequired(), Email()])
    Password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=8, max=50)]
    )
    submit = SubmitField("Submit")


# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    Email = StringField(label="Email", validators=[DataRequired(), Email()])
    Password = PasswordField(
        label="Password", validators=[DataRequired(), Length(min=8, max=50)]
    )
    submit = SubmitField("Let me in")


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    CommentField = CKEditorField("Comment", validators=[DataRequired()])

    submit = SubmitField("Submit ")
