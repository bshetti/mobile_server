#!/usr/bin/python

import logging
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from statsd import StatsClient
from logging.config import dictConfig
from logging.handlers import SysLogHandler


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})



import json

statsd = StatsClient(host='localhost',
                     port=8125,
                     prefix='fitcycle-mobile-server',
                     maxudpsize=512)

# REST Client
import requests
from requests.auth import HTTPBasicAuth

from flask import Flask, render_template, jsonify, flash, request
app = Flask(__name__)
app.debug=True

#with open('./mysql.json') as json_data:
#    data=json.load(json_data)
#    mysqlId=data['id']
#    mysqlPassword=data['password']
#    mysqlServer=data['server']
#    print mysqlId, mysqlPassword


# set variables with env variables
fitcycleapi=os.environ['FITCYCLEAPI']


@statsd.timer('mobileapiTimer')
@app.route('/mobile', methods=['GET'])
def get_tasks():
    app.logger.info('getting all records')
    to_conn_str = 'http://%s'%(fitcycleapi)
#    print('in getting from api_server %s', to_conn_str)
    statsd.incr('mobileCall', rate=1)
    r = requests.get(to_conn_str)
#    print('post request.get', r.status_code)
#    print('output is', r.json())
 
    return r.text


@app.route('/')
def hello_world(name=None):
	return render_template('hello.html') 


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)

