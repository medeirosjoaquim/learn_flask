from flask import Flask
import psycopg2
import psycopg2.extras
from psycopg2 import sql
from flas_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://api_server:docker@localhost/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def hello_world():
    return 'Hello, World!'