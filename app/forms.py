# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2020 -zinken7
"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextField, PasswordField, IntegerField, SelectField
from wtforms.validators import InputRequired, Email, DataRequired, Length

## login and registration

class LoginForm(FlaskForm):
    username = TextField    ('Username', id='username_login'   , validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login'        , validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
    username = TextField('Username'     , id='username_create' , validators=[DataRequired()])
    email    = StringField('Email'      , id='email_create'    , validators=[DataRequired(), Email(message=('Not a valid email address.'))])
    password = PasswordField('Password' , id='pwd_create'      , validators=[DataRequired()])

class CreateProductForm(FlaskForm):
    productname = TextField('Productname',	id='input_productname'  , validators=[DataRequired()])
    price 		= IntegerField('Price'	 , 	id='input_price'   		, validators=[DataRequired()])
    sku 		= TextField('SKU'		 , 	id='input_sku'   		, validators=[DataRequired()])

class CreateCustomerForm(FlaskForm):
    customername = TextField('Customername'	,	id='input_customername' , validators=[DataRequired()])
    email    	 = StringField('Email'		, 	id='input_email'    	)
    phone 		 = IntegerField('Phone'		, 	id='input_phone'   		, validators=[DataRequired()])
    city 		 = SelectField('City'		, 	id='input_city'   		, validators=[DataRequired()]	, choices=["Hà Nội", "Nghệ An", "Hà Tĩnh"],)
    district 	 = SelectField('District'	, 	id='input_district'   	, validators=[DataRequired()]	, choices=["Diễn Châu", "Nghi Lộc", "Ba Đình"],)
    ward 		 = SelectField('Ward'		, 	id='input_ward'   		, choices=["Diễn Tháp", "Nghi Hương", "Nhân Chính"],)
    village 	 = TextField('Village'		, 	id='input_village'   	, validators=[DataRequired()])
