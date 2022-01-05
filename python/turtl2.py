import turtle
t = turtle.Pen()
t.goto(-200,-200)
while t.xcor()<=200:
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)
turtle.done()