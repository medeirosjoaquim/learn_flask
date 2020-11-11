from flask import Flask
import psycopg2
import psycopg2.extras
from psycopg2 import sql
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@localhost/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def hello_world():
    return 'Hello, World!'