import math
from VC1520 import VC1520

plotter = VC1520(6)

L = 30
R = 80

plotter.home()
plotter.lower_case(True)

plotter.color('blue')
plotter.size(2)
plotter.write("Spiro - 2016 - Johan VdB\r")
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
