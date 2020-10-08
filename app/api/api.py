# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2020 -zinken7
"""

from app.api import blueprint
from flask import render_template, redirect, url_for, request, jsonify, abort
from flask_login import login_required, current_user
from app import login_manager, db
from werkzeug.utils import secure_filename

from app.forms import CreateProductForm, CreateCustomerForm
from app.models import Product, Customer

import collections, psycopg2, os

from flask import current_app as app

## Index dashboard
@blueprint.route('/upload', methods=['GET', 'POST'])
def upload_image():

	if request.method == "POST":
		if 'files[0]' not in request.files:
			return abort(404)

		for i in range(len(request.files)):
			fileStorageObj = request.files['files['+str(i)+']']
			filename = secure_filename(fileStorageObj.filename)
			fileStorageObj.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

		return {'status': 'done'}

	return {'status': 'error'}