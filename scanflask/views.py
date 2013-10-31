from flask import render_template
from scanflask import app
from scanflask.forms import ScanForm

app.config.from_object('config')

@app.route('/scan', methods=('GET', 'POST'))
def scan():
  form = ScanForm()
  if form.validate_on_submit():
    return "Valid!~"
  return render_template('scan.html', form=form)

@app.route('/results')
def results():
  scans = []
  scans.append({'ip': '192.168.1.1', 'ports': {80: 'info', 8080: 'more info'}, 'os': 'linux', 'time': '30/Oct/2013 15:08:06', 'hostname': 'bburn1m2'})
  scans.append({'ip': '192.168.1.1', 'ports': {80: 'info', 8080: 'more info'}, 'os': 'linux', 'time': '30/Oct/2013 15:08:06', 'hostname': 'bburn1m2'})
  return render_template('results.html', scans = scans)