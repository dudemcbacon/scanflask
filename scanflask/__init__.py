from flask import Flask
from flask.ext.script import Manager
import redis

app = Flask(__name__)
app.config.from_object('config')

manager = Manager(app)

store = redis.StrictRedis(host='localhost', port=6378, db=0)

from scanflask import views