#!/usr/bin/env python3
"""
Documentation

See also https://www.python-boilerplate.com/flask
"""
import os

from flask import Flask, jsonify
from flask_cors import CORS
from logzero import logger
from num2words import num2words

def fib(n):
  if n<=1:
    return 1
  else:
    return fib(n-2) + fib(n-1)

app = Flask(__name__)
def create_app(config=None):
    # See http://flask.pocoo.org/docs/latest/config/
    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    # Setup cors headers to allow all domains
    # https://flask-cors.readthedocs.io/en/latest/
    CORS(app)

    # Definition of the routes. Put them into their own file. See also
    # Flask Blueprints: http://flask.pocoo.org/docs/latest/blueprints
    @app.route("/")
    def hello_world():
        logger.info("/")
        return "Hello World"

    @app.route("/echo/<someId>")
    def echo_arg(someId):
        logger.info("/foo/%s", someId)
        return jsonify({"echo": someId})
    
    @app.route("/api/numtoword/<int:request_number>")
    def convert_to_thai_word(request_number):
        logger.info("request_number --> %d", request_number)
        return jsonify({
            "th_word": num2words(request_number, lang="th"),
            "en_word": num2words(request_number, lang="en")
        })
   
    return app


if __name__ == "__main__":
    port = int(os.environ.get("FLASK_PORT", default=8000))
    host = str(os.environ.get("FLASK_HOST", default="localhost"))
    app = create_app()
    app.run(host=host, port=port)
