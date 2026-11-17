#Desenhar uma flor
import turtle as t

t.bgcolor("#F5E1F8")
t.pencolor("purple")
t.title("Flor")
t.shape("turtle")
t.speed(0)
t.width(3)

def form(x):
    t.circle(100,x)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.circle(-100,x)

def leaf():
    for i in range(0,140,10):
        form(i)

leaf()
t.setheading(90)
leaf()
t.setheading(180)
leaf()
t.setheading(270)
leaf()
t.exitonclick()
t.done()