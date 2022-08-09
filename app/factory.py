"""
Create and add namespace to Flask app.
"""
from flask import Flask
from flask_restx import Api

from resources.hello import ns_hello


def create_app(name, config):
    """Create and return flask app."""
    app = Flask(name)
    app.config.from_object(config)

    api = Api(
        app,
        version="0.1",
        title="My Blog API",
        doc="/api/docs/",
    )

    api.add_namespace(ns_hello, '/hello')

    return app
