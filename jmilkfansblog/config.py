# -*- coding: UTF-8 -*-
class Config(object):
    """Base config class."""
    SECRET_KEY = 'ccec1c85f0d323bb5d92d25cc7d03a6d'

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    # Open the DEBUG
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/jmilkfansblog'