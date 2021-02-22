import subprocess
from flask import Flask
from flask import render_template
from flask import Markup

app = Flask(__name__)
@app.route('/')
def index():
    check_output = subprocess.check_output("/home/vhserver/vhserver dt | aha --black --no-header", shell=True).decode("utf-8")
    output = str(check_output).replace("\\n", "<br/>")
    html_detail_output = Markup(output)

    template = render_template('main.html', body=html_detail_output)
    return template

@app.route('/start')
def start():
    check_output = subprocess.check_output("/home/vhserver/vhserver st | aha --black --no-header", shell=True).decode("utf-8")
    return render_template('main.html', body = Markup(check_output))

