# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2020 -zinken7
"""

from app.website import blueprint
from flask import render_template, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from app import login_manager, db
from jinja2 import TemplateNotFound

from app.forms import CreateProductForm, CreateCustomerForm
from app.models import Product, Customer

import collections, psycopg2
from   decouple import config

## Index dashboard
@blueprint.route('/')
def index():
    return render_template('website/index.html')

## Other pages
@blueprint.route('/<template>/')
def route_template(template):
    try:

        if not template.endswith( '.html' ):
            template = 'website/' + template + '.html'

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( template, segment=segment )

    except TemplateNotFound:
        return render_template('errors/page_404.html'), 404
    
    except:
        return render_template('errors/page_500.html'), 500

# Extract current page name from request 
def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if request.path == '/':
            segment = 'index'
        elif segment == '':
            segment = request.path.split('/')[-2]

        return segment    

    except:
        return None  