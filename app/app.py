"""
Flask app main module.
"""
from factory import create_app
from database import db
from config import Config


app = create_app(__name__, Config)

db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()
