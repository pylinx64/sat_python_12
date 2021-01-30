import turtle

colors = ['#64FFB9', '#EBA639', '#356BE9', '#35E956', '#DD35E9']
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(100)

text = turtle.textinput('Подсказка 1', 'Подсказка 2')

for i in range(1000):
	print(i)
	t.pencolor(colors[i%5])
	t.penup()
	t.forward(i * 10)
	t.pendown()
	t.write(text, font=('PerfectDOSVGA437', int((i + 4) / 4)))
	t.left(72)
	
