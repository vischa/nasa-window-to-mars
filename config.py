import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
        NASA_API_KEY = os.environ.get('NASA_API_KEY')
