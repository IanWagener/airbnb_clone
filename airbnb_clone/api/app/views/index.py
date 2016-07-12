from flask_json import FlaskJSON, json_response
from datetime import datetime, tzinfo
from pytz import utc, timezone
from app import app, models
from peewee import *

local_tz = timezone('America/Los_Angeles')

@app.route('/', methods=['GET'])
def index():
    return json_response(status="OK", utc_time=datetime.utcnow().strftime('%m/%d/%Y %H:%M:%S'), time=utc_to_local(datetime.utcnow()).strftime('%m/%d/%Y %H:%M:%S')) #format 2nd arg into UTC

@app.errorhandler(404)
def not_found(e):
    return json_response(add_status_=False, code=404, msg="not found")

def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)

def before_request():
    models.database.connect()

def after_request():
    models.database.close()
