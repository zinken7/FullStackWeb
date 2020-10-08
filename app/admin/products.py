# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2020 -zinken7
"""

from app.home import blueprint
from flask import render_template, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from app import login_manager, db
from jinja2 import TemplateNotFound

from app.base.forms import CreateProductForm, CreateCustomerForm
from app.base.models import Product, Customer

import collections, psycopg2
from   decouple import config

## Index dashboard
@blueprint.route('/index')
def index():
    return render_template('index.html')

## CRUD product
@blueprint.route('/api/product', methods=['POST','GET'])
def product():
    
    # GET product info from database
    if request.method == 'GET':
        conn_string = "host="+config('DB_HOST')+" dbname="+config('DB_NAME')+" user="+config('DB_USERNAME')+" password="+config('DB_PASS')
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        # Convert query to objects of key-value pairs
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d["productname"] = [row[1], row[0]]
            d["price"] = row[2]
            d["sku"] = row[3]
            d["id"] = row[0]
            objects_list.append(d)

        response = jsonify(data=objects_list)
        conn.close()

        return response
    # POST product to database
    elif request.method == 'POST':
        form = CreateProductForm(request.form)
        if form.validate_on_submit():
            # read form data
            productname = request.form['productname']
            price = request.form['price']
            sku = request.form['sku']
            # else we can create the product
            product = Product(**request.form)
            db.session.add(product)
            db.session.commit()

            response = jsonify(title="Success! ", message="Bạn đã tạo sản phẩm mới thành công", status="success")
            return response
        else:
            return jsonify(title="Fail! ", message="Tạo mới sản phẩm không thành công", status="danger")


@blueprint.route('/api/product/<string:id>', methods=['GET','PUT','DELETE'])
def oneproduct(id):

    # GET one product from database
    if request.method == 'GET':
        showData = Product.query.get(id)
        data = {
            "productname": showData.productname,
            "price": showData.price,
            "sku": showData.sku
        }

        return jsonify(data)
    
    # UPDATE product to database
    elif request.method == 'PUT':
        form = CreateProductForm(request.form)
        if form.validate_on_submit():
            # read form data
            n_productname = request.form['productname']
            n_price = request.form['price']
            n_sku = request.form['sku']
            # else we can update the product
            editData = Product.query.filter_by(id=id).first()
            editData.productname = n_productname
            editData.price = n_price
            editData.sku = n_sku
            db.session.commit()

            response = jsonify(title="Success! ", message="Bạn đã sửa thông tin thành công", status="success")

            return response
        else:
            return jsonify(title="Fail! ", message="Sửa thông tin sản phẩm không thành công", status="danger")
    
    # DELETE product from database
    elif request.method == 'DELETE':
        try:
            delData = Product.query.filter_by(id=id).first()
            db.session.delete(delData)
            db.session.commit()
            response = jsonify(title="Success! ", message="Bạn đã xoá sản phẩm thành công", status="success")
            return response
        except:
            return jsonify(title="Fail! ", message="Xoá sản phẩm không thành công", status="danger")


## CRUD Customer
@blueprint.route('/api/customer', methods=['POST','GET'])
def customer():
    
    # GET customer info from database
    if request.method == 'GET':
        conn_string = "host="+config('DB_HOST')+" dbname="+config('DB_NAME')+" user="+config('DB_USERNAME')+" password="+config('DB_PASS')
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()

        # Convert query to objects of key-value pairs
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d["customername"] = [row[1], row[0]]
            d["email"] = row[2]
            d["phone"] = row[3]
            d["city"] = row[4]
            d["district"] = row[5]
            d["ward"] = row[6]
            d["village"] = row[7]
            d["id"] = row[0]
            objects_list.append(d)

        response = jsonify(data=objects_list)
        conn.close()

        return response
    # POST customer to database
    elif request.method == 'POST':
        form = CreateCustomerForm(request.form)
        if form.validate_on_submit():
            # read form data
            customername = request.form['customername'].title()
            email = request.form['email']
            phone = request.form['phone']
            city = request.form['city']
            district = request.form['district']
            ward = request.form['ward']
            village = request.form['village']
            # else we can create the customer
            customer = Customer(customername, email, phone, city, district, ward, village)
            db.session.add(customer)
            db.session.commit()

            response = jsonify(title="Success! ", message="Bạn đã thêm khách hàng mới thành công", status="success")
            return response
        else:
            return jsonify(title="Fail! ", message="Thêm mới khách hàng không thành công", status="danger")


@blueprint.route('/api/customer/<string:id>', methods=['GET','PUT','DELETE'])
def onecustomer(id):

    # GET one customer from database
    if request.method == 'GET':
        showData = Customer.query.get(id)
        data = {
            "customername": showData.customername,
            "email": showData.email,
            "phone": showData.phone,
            "city": showData.city,
            "district": showData.district,
            "ward": showData.ward,
            "village": showData.village,
        }

        return jsonify(data)
    
    # UPDATE customer to database
    elif request.method == 'PUT':
        form = CreateCustomerForm(request.form)
        if form.validate_on_submit():
            # read form data
            n_customername = request.form['customername']
            n_email = request.form['email']
            n_phone = request.form['phone']
            n_city = request.form['city']
            n_district = request.form['district']
            n_ward = request.form['ward']
            n_village = request.form['village']
            # else we can update the customer
            editData = Customer.query.filter_by(id=id).first()
            editData.customername = n_customername.title()
            editData.email = n_email
            editData.phone = n_phone
            editData.city = n_city
            editData.district = n_district
            editData.ward = n_ward
            editData.village = n_village
            db.session.commit()

            response = jsonify(title="Success! ", message="Bạn đã sửa thông tin khách hàng thành công", status="success")

            return response
        else:
            return jsonify(title="Fail! ", message="Sửa thông tin khách hàng không thành công", status="danger")
    
    # DELETE customer from database
    elif request.method == 'DELETE':
        try:
            delData = Customer.query.filter_by(id=id).first()
            db.session.delete(delData)
            db.session.commit()
            response = jsonify(title="Success! ", message="Bạn đã xoá khách hàng thành công", status="success")
            return response
        except:
            return jsonify(title="Fail! ", message="Xoá khách hàng không thành công", status="danger")


## Customer pages
@blueprint.route('/customer')
def customers():
    form = CreateCustomerForm(request.form)
    return render_template('customer.html', form=form)

## Product pages
@blueprint.route('/tables')
def products():
    form = CreateProductForm(request.form)
    return render_template('tables.html', form=form)

## Other pages
@blueprint.route('/<template>')
def route_template(template):
    try:
        return render_template(template + '.html')

    except TemplateNotFound:
        return render_template('errors/page_404.html'), 404
    
    except:
        return render_template('errors/page_500.html'), 500
