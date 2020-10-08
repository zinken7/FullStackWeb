# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2020 - zinken7
"""
import os
from   decouple import config

class Config(object):

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='Secretinconfigfile')
    UPLOAD_FOLDER = 'app/static/assets/uploads'
    ALLOWED_EXTENSIONS = {'csv', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY  = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config( 'DB_ENGINE'   , default='postgresql'    ),
        config( 'DB_USERNAME' , default='postgres'      ),
        config( 'DB_PASS'     , default='postgres'      ),
        config( 'DB_HOST'     , default='localhost'     ),
        config( 'DB_PORT'     , default=5432            ),
        config( 'DB_NAME'     , default='dashboard-pro' )
    )

class DebugConfig(Config):
    DEBUG = True

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config( 'DB_ENGINE'   , default='postgresql'    ),
        config( 'DB_USERNAME' , default='postgres'      ),
        config( 'DB_PASS'     , default='postgres'      ),
        config( 'DB_HOST'     , default='localhost'     ),
        config( 'DB_PORT'     , default=5432            ),
        config( 'DB_NAME'     , default='dashboard-dev' )
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}