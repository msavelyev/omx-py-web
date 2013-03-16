from flask import Flask
from flask import render_template
from flask import request
import os
import subprocess
import time
import signal
import itertools
import config
from omxwrapper import omxwrapper

app = Flask('hello')
omx = omxwrapper(config.omx_options)

def list_files(path):
    for root, dirs, files in os.walk(path):
        subdirs = [list_files(os.path.join(root, d)) for d in dirs]
        return [os.path.join(root, f) for f in files] + list(itertools.chain.from_iterable(subdirs))

@app.route('/cmd/play')
def cmd_play():
    filename = request.args.get('filename', None)
    omx.play(config.media + filename)
    return 'ok'

@app.route('/cmd/stop')
def cmd_stop():
    omx.stop()
    return 'ok'

@app.route('/cmd/pause')
def cmd_pause():
    omx.pause()
    return 'ok'

@app.route('/')
def main():
    files = [f.replace(config.media, '') for f in list_files(config.media)]
    files.sort()

    return render_template(
        'main.html',
        files = files,
        playing = omx.filename.replace(config.media, '') if omx.playing else None,
        paused = omx.paused
    )

if __name__ == '__main__':
    app.debug = True
    app.run(host = config.bind_host, port = config.port)

