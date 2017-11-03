import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print(basedir)


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hardtoguessstring"
    MONGO2_DBNAME = 'data_lei'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,
                                                                                                'data-dev.sqlite')


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}
