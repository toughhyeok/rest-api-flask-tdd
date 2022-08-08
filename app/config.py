"""
Configuration module.
"""
import os


db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')

SQLALCHEMY_DATABASE_URI = \
    f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}/{db_name}'


class Config(object):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        "execution_options": {
            "schema_translate_map": {
                "flask": None
            }
        }
    }
