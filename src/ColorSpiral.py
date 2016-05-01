#ColorSpiral.py
import turtle as turtly
t=turtly.Pen()
turtly.bgcolor("white")
# You can choose between 1 and 1000 sides for cool shapes!
sides=10
colors=['pink', 'purple', 'blue', 'yellow', 'green', 'cyan', 'turquoise', 'red', 'violet', 'salmon']
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 5/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
