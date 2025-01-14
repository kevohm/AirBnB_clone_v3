#!/usr/bin/python3
"""flask app"""
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def db_close(exc):
    """ close the database """
    storage.close()


@app.errorhandler(404)
def server_error(err):
    """ Handle unavailabe route"""
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == '__main__':
    app.run(host=getenv("HBNB_API_HOST") or '0.0.0.0',
            port=getenv("HBNB_API_PORT") or '5000', threaded=True)
