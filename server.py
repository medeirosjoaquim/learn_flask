from flask import Flask, request
import psycopg2
import psycopg2.extras
from psycopg2 import sql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from flask.templating import render_template

Base = declarative_base()

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@appdb/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(100))
    #completed = Column(Boolean)

    def __init__(self, title, description, completed):
        self.title = title
        self.description = description
        self.completed = completed
    def __repr__(self):
            return '<Tasks {}>'.format(self.title)

@app.route('/create')
def create():
        title = request.args.get('title')
        description = request.args.get('description')
        completed = request.args.get('completed')
        completed_value = False
        if completed == 'true':
            completed_value = True
        data = Tasks(title, description, completed_value)
        db.session.add(data)
        db.session.commit()
        return 'success'
    
@app.route('/')
def index():
    return 'hello'



@app.route('/test')
def test():
    return render_template('index.html', tasks = Tasks.query.all())
