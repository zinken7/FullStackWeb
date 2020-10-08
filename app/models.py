# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2020 -zinken7
"""

from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String, Float

from app import db, login_manager

from app.auth.util import hash_pass

class User(db.Model, UserMixin):

    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(Binary)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass( value ) # we need bytes here (not plain str)
                
            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None


class Product(db.Model, UserMixin):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    productname = Column(String, unique=True)
    price = Column(Float, unique=True)
    sku = Column(String, unique=True)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]
                
            setattr(self, property, value)

    def __repr__(self):
        return str(self.productname)


class Customer(db.Model, UserMixin):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    customername = Column(String)
    email = Column(String, unique=True)
    phone = Column(Integer, unique=True)
    city = Column(String)
    district = Column(String)
    ward = Column(String)
    village = Column(String)

    def __init__(self, customername, email, phone, city, district, ward, village):
        self.customername = customername
        self.email = email
        self.phone = phone
        self.city = city
        self.district = district
        self.ward = ward
        self.village = village

    def __repr__(self):
        return '<id {}>'.format(self.id)
