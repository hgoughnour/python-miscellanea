#NiceHexSpiral.py
import turtle
colors=['purple', 'cyan', 'turquoise', 'blue', 'yellow', 'pink']
t=turtle.Pen()
turtle.bgcolor('orange')
for x in range (360):
       t.pencolor(colors[x%6])
       t.width(x/100+1)
       t.forward(x)
       t.left(1000000000%360)
