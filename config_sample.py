from logging import ERROR, CRITICAL


class Config(object):
    DEBUG = True
    TESTING = False
    SERVER_NAME = '127.0.0.1:8000'
    FILE_LOGGER = {
        'format': '%(asctime)s %(levelname)s: %(message)s in %(pathname)s:%(funcName)s:%(lineno)d',
        'location': 'app.log',
        'level': ERROR,
        'duration': 'D',
        'backup': 30,

    }
    EMAIL_LOGGER = {
        'recipients': [''],
        'server': '',
        'sender': 'error@craftsvilla.com',
        'level': CRITICAL,
        'subject': 'Product Page Failed!',
        'format': '''
    Message type:       %(levelname)s
    Location:           %(pathname)s:%(lineno)d
    Module:             %(module)s
    Function:           %(funcName)s
    Time:               %(asctime)s

    Message:

    %(message)s
    '''
    }


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    REDIS = {
        'server': '',
        'port': 6379,
        'user_name': '',
        'password': '',
    }
    MYSQL = {
        'server': '',
        'port': 3306,
        'user_name': '',
        'password': '',
    }
    ELASTIC_SEARCH = {
        'api': '',
    }


class DevelopmentConfig(Config):
    DEBUG = True
    SERVER_NAME = '127.0.0.1:8000'
    REDIS = {
        'server': '',
        'port': 6379,
        'user_name': '',
        'password': '',
    }
    MYSQL = {
        'server': '',
        'port': 3306,
        'user_name': '',
        'password': '',
    }
    ELASTIC_SEARCH = {
        'api': '',
    }


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    REDIS = {
        'server': '',
        'port': 6379,
        'user_name': '',
        'password': '',
    }
    MYSQL = {
        'server': '',
        'port': 3306,
        'user_name': '',
        'password': '',
    }
    ELASTIC_SEARCH = {
        'api': '',
    }
