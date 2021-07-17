import turtle
descendente = int(input('Digite quantos degraus descendentes você quer:'))
ascendente = int(input('Digite quantos degraus ascendentes você quer:'))
t = turtle.Turtle()
condicao1 = range(descendente)
condicao2 = range(ascendente)
#descendente
for i in condicao1:
    t.color('blue')
    t.begin_fill()
    for j in range(2):
        t.forward(50)
        t.right(90)
        t.forward(25)
        t.right(90)
    t.penup()
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.pendown()
    t.end_fill()
#ascendente
for i in condicao2:
    t.forward(25)
    t.color('blue')
    t.fillcolor('red')
    t.begin_fill()
    for j in range(2):
        t.forward(50)
        t.left(90)
        t.forward(25)
        t.left(90)
    t.penup()
    t.left(90)
    t.forward(25)
    t.right(90)
    t.pendown()
    t.end_fill()
