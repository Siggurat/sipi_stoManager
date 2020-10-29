from datetime import datetime
import uuid
from flask_security import UserMixin, RoleMixin

from extensions import db


def _generate_unique_track_number() -> str:
    unique_string = uuid.uuid4().hex[:16]
    track_number = '-'.join(unique_string[i:i + 4] for i in range(0, len(unique_string), 4)).upper()
    return track_number


class CarBrand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'{self.name}'


class CarModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    car_brand_id = db.Column(db.Integer, db.ForeignKey('car_brand.id'), nullable=False)
    car_brand = db.relationship('CarBrand')

    def __repr__(self):
        return f'{self.name}'


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f'{self.name}'


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    tel = db.Column(db.String(19), nullable=False)
    car_brand_id = db.Column(db.Integer, db.ForeignKey('car_brand.id'), nullable=False)
    car_brand = db.relationship('CarBrand')
    car_model_id = db.Column(db.Integer, db.ForeignKey('car_model.id'), nullable=False)
    car_model = db.relationship('CarModel')
    unique_track_number = db.Column(db.Integer, default=_generate_unique_track_number)
    date = db.Column(db.DateTime, default=datetime.now())
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), default=1)
    status = db.relationship('Status')

    def __repr__(self):
        return f'<Application id: {self.id}, Name: {self.name}, Last name: {self.last_name}, E-mail: {self.email},' \
               f' Telephone number: {self.tel}, Car brand id: {self.car_brand_id}, Car model id: {self.car_model_id}, ' \
               f'Date: {self.date} '

    def serialize(self):
        result = {
            'track_number': self.unique_track_number,
            'car_brand': self.car_brand.name,
            'car_model': self.car_model.name,
            'price': self.car_model.price,
            'date': self.date,
            'status': self.status.name
        }
        return result


# Flask Security

roles_users_table = db.Table('roles_users',
                             db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                             db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
                             )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean)
    roles = db.relationship('Role', secondary=roles_users_table, backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
