from flask import Flask
import psycopg2
import psycopg2.extras
from psycopg2 import sql
from DBUtils.PersistentDB import PersistentDB

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


DATABASE = PersistentDB(
    psycopg2,
    host=Settings.get_setting('DB_HOST'),
    user=Settings.get_setting('DB_USERNAME'),
    password=Settings.get_setting('DB_PASSWORD'),
    dbname=Settings.get_setting('DB'),
    cursor_factory=psycopg2.extras.RealDictCursor)    