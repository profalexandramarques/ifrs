#Programa simples da tartaruga
import turtle as t

t.title("Tartaruga")
t.speed(10)
t.pensize(1)
t.pencolor("purple")
t.fillcolor("green")
#Tipo tartaruga
t.shape("turtle")
#Tamanho da tartaruga
t.shapesize(1,1,1)
t.width(3)
t.right(90)
t.forward(100)
t.left(90)
t.backward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
#Desenha um circulo
t.circle(60)
#Desenha uma reta
t.goto(150,50)
t.done()