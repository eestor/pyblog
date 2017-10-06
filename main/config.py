import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    'Base config class'
    DEBUG = True
    TESTING = False
    FLASKY_POSTS_PER_PAGE = 10
    FLASKY_COMMENTS_PER_PAGE = 10
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    OAUTH_CREDENTIALS = {
        'facebook': {
            'id': '279444199215077',
            'secret': '9fb107214bbbed607bd8d8ec0d8f263b'
        },
        'twitter': {
            'id': '3RzWQclolxWZIMq5LJqzRZPTl',
            'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
        }
    }


class ProductionConfig(BaseConfig):
    'Production specific config'
    DEBUG = False
    #SECRET_KEY = open('/path/to/secret/file').read()
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class StagingConfig(BaseConfig):
    'Staging specific config'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class DevelopmentConfig(BaseConfig):
    'Development environment specific config'
    DEBUG = False
    TESTING = True
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data2-dev.sqlite')
    #SQLALCHEMY_DATABASE_URI =  'sqlite:////tmp/test.db'
    Profile = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

