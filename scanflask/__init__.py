from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
app.config.from_object('config')

manager = Manager(app)

from scanflask import views