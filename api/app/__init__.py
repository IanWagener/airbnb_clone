from flask import Flask
from flask_json import FlaskJSON
import config

__all__ = ["config"]

# Initialize Flask application
app = Flask(__name__)

# Initialize FlaskJSON instance with Flask app
FlaskJSON(app)
