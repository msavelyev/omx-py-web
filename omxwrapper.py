import os
import subprocess

class omxwrapper:
    def __init__(self, options):
        self.options = options

        self.playing = False
        self.paused = False
        self.filename = None
        self.r = None
        self.w = None

    def _send(self, char):
        print 'sending %s' % char
        os.write(self.w, char)

    def stop(self):
        if self.playing:
            self._send('q')

            self.filename = None
            self.playing = False
            self.paused = False

    def play(self, filename):
        self.stop()

        self.r, self.w = os.pipe()

        params = ['omxplayer'] + self.options + [filename]
        print 'params %s' % params

        subprocess.Popen(params,\
            stdin = os.fdopen(self.r, 'r'), \
            stdout = subprocess.PIPE, \
            stderr = subprocess.PIPE)

        self.filename = filename
        self.paused = False
        self.playing = True

    def pause(self):
        if self.playing:
            self.paused = not self.paused
            self._send('p')


