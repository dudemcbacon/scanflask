from nmap-flask import app

@add.route('/')
@add.route('/index')
def index():
  return str('Hello World')