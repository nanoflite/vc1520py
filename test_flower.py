from VC1520 import VC1520

plotter = VC1520(6)

plotter.home()
plotter.lower_case(True)
plotter.color('blue')
plotter.size(1)
plotter.puts("Flower by Johan VdB - 2016\r")

with open('assets/flower.txt') as f:
    for line in f:
        parts = line.split(",")

        y = int(parts[1])
        print "%d %s" %(y, parts[0])
        plotter.color(parts[0])

        count = int(parts[2]) / 2
        for i in range(0, count):
            x1 = int(parts[3+2*i+0])
            x2 = int(parts[3+2*i+1])
            plotter.move(x1, -1*y)
            plotter.draw(x2, -1*y)
