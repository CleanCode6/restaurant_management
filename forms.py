from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.core import FloatField  # FieldList
from wtforms.fields.simple import FileField
from wtforms.validators import DataRequired, Length

from fields import JSONField


class RestaurantForm(FlaskForm):
    restaurant_name = StringField(label=('Name'), validators=[DataRequired(), Length(max=80, message='You cannot have more than 80 characters')])
    # distance = StringField(label=('Distance'), validators=[DataRequired(), Length(max=100, message='You cannot have more than 100 characters')]) 
    category = StringField(label=('Category (0: 한식, 1: 중식, 2: 양식, 3: 일식, 4: 카페)'), validators=[DataRequired(), Length(max=20, message='You cannot have more than 20 characters')])
    description = StringField(label=('Content'), validators=[DataRequired(), Length(max=2000, message='You cannot have more than 2000 characters')])
    score = FloatField(label=('Score'), validators=[DataRequired()])
    # pricing = StringField(label=('Pricing'), validators=[DataRequired(), Length(max=100, message='You cannot have more than 100 characters')])
    image = FileField(label=('Image'), validators=[DataRequired()])
    # phone = StringField(label=('Phone'), validators=[DataRequired(), Length(max=200, message='You cannot have more than 200 characters')])
    menu = JSONField(label=('Menu'))  # , validators=[DataRequired()]
    position_x = FloatField(label=('Position_x'), validators=[DataRequired()])
    position_y = FloatField(label=('Position_y'), validators=[DataRequired()])
    address = StringField(label=('Address'), validators=[DataRequired(), Length(max=200, message='You cannot have more than 200 characters')])