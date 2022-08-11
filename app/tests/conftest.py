"""
Configuration tests for flask app.
"""
import pytest

from factory import create_app
from database import db
from config import TestingConfig


@pytest.fixture(scope='session')
def app():
    """Create and return flask app for test."""
    app = create_app('test', TestingConfig)
    db.init_app(app)

    ctx = app.app_context()
    ctx.push()

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()

    db.session.remove()
    ctx.pop()


@pytest.fixture(scope='session')
def client(app):
    """return test client."""
    return app.test_client()
