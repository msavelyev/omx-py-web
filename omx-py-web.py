from flask import Flask
from flask import render_template
from flask import request
import os
import subprocess
import time
import signal
import itertools

app = Flask('hello')

path = '/mnt/usb/downloads/'

def list_files(path):
    for root, dirs, files in os.walk(path):
        subdirs = [list_files(os.path.join(root, d)) for d in dirs]
        return [os.path.join(root, f) for f in files] + list(itertools.chain.from_iterable(subdirs))

r = None
w = None

paused = False
playing = None

def play(filename):
    global r, w

    r, w = os.pipe()

    subprocess.Popen(['omxplayer', '-o', 'hdmi', '-r', filename],\
        stdin = os.fdopen(r, 'r'), \
        stdout = subprocess.PIPE, \
        stderr = subprocess.PIPE)

    print 'playing ' + filename

def stop():
    global playing

    if playing:
        print 'terminating'
        send('q')
        playing = None
        paused = False

def send(char):
    global w

    print 'sending ' + char
    os.write(w, char)

@app.route('/cmd/play')
def cmd_play():
    global playing, paused

    stop()

    filename = request.args.get('filename', None)

    playing = filename
    paused = False

    play(path + filename)
    return 'ok'

@app.route('/cmd/stop')
def cmd_stop():
    stop()
    return 'ok'

@app.route('/cmd/pause')
def cmd_pause():
    global paused

    paused = not paused

    send('p')
    return 'ok'


@app.route('/')
def hello_world():
    global playing, paused

    files = [f.replace(path, '') for f in list_files(path)]
    files.sort()

    return render_template(
        'main.html',
        msg = 'It works! yeah',
        files = files,
        playing = playing,
        paused = paused
    )

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0')

