from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, Email
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from models import CarBrand, CarModel


def get_car_brand():
    return CarBrand.query.all()


def get_car_model():
    return CarModel.query.all()


class ApplicationForm(FlaskForm):
    car_brand = QuerySelectField(
        u'Марка машины:',
        query_factory=get_car_brand,
        allow_blank=True,
        blank_text=u'Выберите марку',
        validators=[
            DataRequired('Вы не выбрали марку машины')
        ]
    )
    car_model = QuerySelectField(
        u'Выберите модель:',
        query_factory=get_car_model,
        allow_blank=True,
        blank_text=u'Выберите модель',
        render_kw={'disabled': 'disabled'},
        validators=[
            DataRequired('Вы не выбрали модель машины')
        ]
    )
    name = StringField(
        u'Имя:',
        render_kw={'placeholder': 'Введите имя'},
        validators=[
            DataRequired('Введите Ваше имя'),
            Length(max=40, message='Имя не должно превышать 40 символов'),
            Regexp('^\D+$', message='Имя должно состоять из символов кириллицы или латиницы')
        ]
    )
    last_name = StringField(
        u'Фамилия:',
        render_kw={'placeholder': 'Введите фамилию'},
        validators=[
            DataRequired('Введите Вашу фамилию'),
            Length(max=70, message='Фамилия не должна превышать 70 символов'),
            Regexp('^\D+$', message='Фамилия должна состоять из символов кириллицы или латиницы')
        ]
    )
    email = StringField(
        u'E-mail:',
        render_kw={'placeholder': 'Введите E-mail'},
        validators=[
            DataRequired('Введите Вашу электронную почту'),
            Email(message='Введите верный E-mail')
        ]
    )
    tel = StringField(
        u'Номер телефона:',
        render_kw={'placeholder': 'Введите номер телефона'},
        validators=[
            DataRequired('Введите Ваш номер телефона'),
            Length(min=18, max=18, message='Введите верный номер телефона')
        ]
    )
    submit = SubmitField('Отправить заявку')
