from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired

class ScanForm(Form):
  subnet = TextField('Subnet', validators=[DataRequired()])
  ports = TextField('Ports', validators=[DataRequired()])