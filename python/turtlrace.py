import turtle
import random
a = turtle.Pen()
b = turtle.Pen()
c = turtle.Pen()
a.penup()
b.penup()
c.penup()
a.goto(200, -100)
a.pencolor(0,1,0)
a.pendown()
a.goto(200, 100)
a.penup()
a.goto(-300, 50)
b.goto(-300, -50)
c.goto(-300, 0)
a.pendown()
b.pendown()
c.penup()
a.pencolor(0.8,0.8,1)
b.pencolor(0.8,1,1)
c.pencolor(0,1,1)
a.speed(1)
b.speed(1)
c.speed(1)
step_a = 1
step_b = 1
step_c = 1
while a.xcor()<200 and b.xcor()<200 and c.xcor<200:
    if random.randint(0,1) == 1 and step_a < 7:
        step_a += 1
    elif step_a > 1:
        step_a -= 1
    if random.randint(0,1) == 1 and step_b < 7:
        step_b += 1
    elif step_b > 1:
        step_b -= 1
    if random.randint(0,1) == 1 and step_c < 7:
        step_c += 1
    elif step_c > 1:
        step_c -= 1
    a.fd(step_a)
    b.fd(step_b)
    c.fd(step_c)
if a.xcor()>b.xcor() and a.xcor()>c.xcor():
    b.ht()
    c.ht()
elif b.xcor()>a.xcor() and b.xcor()>c.xcor():
    c.ht()
    a.ht()
elif c.xcor()>b.xcor() and c.xcor()>a.xcor():
    a.ht()
    b.ht()
turtle.done()