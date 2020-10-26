from flask import Flask
import psycopg2
import psycopg2.extras
from psycopg2 import sql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(100))
    completed = Column(Boolean)

    def __init__(self, title, description, completed):
        self.title = title
        self.description = description
        self.completed = completed
    def __repr__(self):
            return '<Tasks {}>'.format(self.title)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    print (Tasks.query.all())
    return "hello"
