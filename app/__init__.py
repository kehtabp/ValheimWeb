import re
import subprocess

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


@app.route('/restart')
def restart():
    command = "/home/vhserver/vhserver r | aha --black --no-header"
    return response(command)


@app.route('/stop')
def stop():
    command = "/home/vhserver/vhserver sp | aha --black --no-header"
    return response(command)


def response(command):
    output = subprocess.check_output("%s" % command, shell=True).decode("utf-8")
    pattern = "Internet IP:\s+</span>(\d+\.\d+\.\d+\.\d+:\d+)"
    try:
        title = "Connect"
        ip = f"steam://run/892970//+connect {re.findall(pattern, output)[0]}"
    except:
        title = "Server Details"
        ip = "/"
    return render_template('main.html', body=Markup(output), ip=ip, title=title)
