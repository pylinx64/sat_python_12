import turtle
import time

list_colors = ["lime", "yellow", "white", "#B0A733"]

pen = turtle.Pen()

turtle.bgcolor('black')

pen.pencolor(list_colors[1])
pen.forward(100)
pen.left(120)

pen.pencolor(list_colors[0])
pen.forward(100)
pen.left(120)

pen.pencolor(list_colors[3])
pen.forward(100)
pen.left(120)

pen.up()
pen.forward(150)
pen.down()

pen.width(100)
pen.forward(100)

time.sleep(100)
