from opencbm import *

class VC1520:

    def __init__(self, dev):
        self.dev = dev
        self.cbm = cbm_open_driver()
        cbm_lock(self.cbm)

    def __del__(self):
        cbm_unlock(self.cbm)
        cbm_close_driver(self.cbm)

    def _write(self, secadr, data):
        cbm_open(self.cbm, self.dev, secadr, "")
        cbm_listen(self.cbm, self.dev, secadr)
        cbm_write(self.cbm, data)
        cbm_unlisten(self.cbm)
        cbm_close(self.cbm, self.dev, secadr)

    def write(self, text):
        self._write(0, text)

    def puts(self, text):
        petscii = cbm_to_petscii(text)
        self._write(0, petscii)

    def home(self):
        self.plot("H")

    def set_relative_origin(self):
        self.plot("I")

    def move(self, x, y):
        self.plot("M", x, y)

    def draw(self, x, y):
        self.plot("D", x, y)

    def move_relative(self, x, y):
        self.plot("R", x, y)

    def draw_relative(self, x, y):
        self.plot("J", x, y)

    def plot(self, command, x = None, y = None):
        cbm_open(self.cbm, self.dev, 1, "")
        cbm_listen(self.cbm, self.dev, 1)
        if x == None:
            cbm_write(self.cbm, command)
        else:
            cbm_write(self.cbm, "%s,%d,%d" % (command, x, y))
        cbm_unlisten(self.cbm)
        cbm_close(self.cbm, self.dev, 1)

    def color(self, col):
        if col == "black":
            _col = 0
        elif col == "blue":
            _col = 1
        elif col == "green":
            _col = 2
        elif col == "red":
            _col = 3
        else:
            _col = col
        self._write(2, "%d" % _col)

    def size(self, siz):
        self._write(3, "%d" % siz)

    def rotate(self, rot):
        if rot:
            value = "1"
        else:
            value = "0"
        self._write(4, value)

    def scribe(self, mode):
        self._write(5, "%d" % mode)

    def lower_case(self, lower):
        if lower:
            value = "1"
        else:
            value = "0"
        self._write(6, value)

    def reset(self):
        self._write(7, "")


