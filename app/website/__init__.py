# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2020 -zinken7
"""

from flask import Blueprint

blueprint = Blueprint(
    'website_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static',
    static_url_path='websites'
)
