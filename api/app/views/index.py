from flask_json import FlaskJSON, json_response
from datetime import datetime, tzinfo
from pytz import utc, timezone
from app import app, models
from peewee import *

local_tz = timezone('America/Los_Angeles')

'''
Function to manage the API route /
allowing only GET request
response will be a JSON
return a hash with those key/value:
status 'OK', utc_time and time
'''
@app.route('/', methods=['GET'])
def index():
    return json_response(status="OK", utc_time=datetime.utcnow().strftime('%m/%d/%Y %H:%M:%S'), time=utc_to_local(datetime.utcnow()).strftime('%m/%d/%Y %H:%M:%S')) #format 2nd arg into UTC

# Function to manage all not found routes
@app.errorhandler(404)
def not_found(e):
    return json_response(add_status_=False, code=404, msg="not found")

def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)

# Function to open a database connection
def before_request():
    models.database.connect()

# Function to close a database connection
def after_request():
    models.database.close()
