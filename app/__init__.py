import subprocess
import re
from flask import Flask
from flask import Markup
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    command = "/home/vhserver/vhserver dt | aha --black --no-header"
    return response(command)


@app.route('/start')
def start():
    command = "/home/vhserver/vhserver st | aha --black --no-header"
    return response(command)


def response(command):
    output = subprocess.check_output("%s" % command, shell=True).decode("utf-8")
    pattern = "Internet IP:\s+</span>(\d+\.\d+\.\d+\.\d+:\d+)"
    ip = re.findall(pattern, output)[0]
    return render_template('main.html', body=Markup(output),ip=ip)
