import turtle

colors = ['#D6FF30', '#30FF6D', '#30E1FF', '#C230FF']
t = turtle.Pen()
turtle.bgcolor('black')

t.shape('turtle')

def side(tangle, width, color): 
	# входные данные: tangle - угол, width - длина линиий, color - номер цвета
	t.pencolor(colors[color])
	t.forward(width)
	t.left(tangle)

side(120, 100, 0)
side(120, 100, 1)
side(120, 100, 2)

turtle.done()
