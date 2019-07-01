"""
2019年 06月 13日 星期四 10:28:37 CST
"""

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=20)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)