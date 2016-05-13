import math
from VC1520 import VC1520

colors = ('black', 'red', 'green', 'blue')

plotter = VC1520(6)

plotter.reset()
plotter.lower_case(True)
plotter.color('black')
plotter.size(1)
plotter.puts("VC1520 demo - 2016 - Johan VdB\r")
plotter.set_relative_origin()
plotter.draw_relative(480,0)
plotter.puts('\r\r')

# -- Font size
plotter.reset()
plotter.lower_case(True)
for size in range(0,4):
    plotter.size(size)
    plotter.color(colors[size])
    plotter.puts("VC1520\r\r")
plotter.set_relative_origin()
plotter.move(0,60)

# -- Scribe line (pattern)
plotter.reset()
plotter.color('black')
plotter.size(1)
for scribe in range(0,16):
    plotter.move(0, -scribe*20)
    plotter.scribe(0)
    plotter.puts("%2d" % scribe)
    plotter.scribe(scribe)
    plotter.move(30, -scribe*20+10)
    plotter.draw(480, -scribe*20+10)
plotter.move(0,-20*(scribe+1))

# -- Grid
plotter.reset()
plotter.color('green')
for y in range(0,9):
    plotter.move(0, -y*55)
    plotter.draw(8*55, -y*55)
plotter.color('blue')
for x in range(0,9):
    plotter.move(x*55, 0)
    plotter.draw(x*55, -8*55)
plotter.move(0,-490)

# -- Spirograph
L = 30
R = 80
plotter.reset()
plotter.move(240, -200)
plotter.set_relative_origin()
for J in range(0, 360, 15):
    for I in range(0, 360, 10):
        X = R*math.sin(J*math.pi/180)+L*math.sin(I*math.pi/180)
        Y = R*math.cos(J*math.pi/180)+L*math.cos(I*math.pi/180)
        if I == 0:
            plotter.move_relative(X, Y)
        else:
            plotter.draw_relative(X, Y)
plotter.move_relative(0, -100)

# -- End
plotter.reset()
plotter.lower_case()
plotter.size(2)
plotter.puts('\r')
i = 0
for c in 'READY':
    plotter.color(colors[i])
    plotter.puts(c)
    i = i+1 if i<3 else 0
plotter.puts('\r')
