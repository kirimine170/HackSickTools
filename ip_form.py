from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, IPAddress

class IPForm(FlaskForm):
    ip_address = StringField('敵を見誤るなよ？（fill in target IP）：', validators=[DataRequired(), IPAddress()])
    submit = SubmitField('submit')