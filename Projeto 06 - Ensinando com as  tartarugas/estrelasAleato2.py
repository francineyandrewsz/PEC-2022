from turtle import *
from random import *

#uma função para mover a tartaruga para uma posição aleatória
def moveToRandomLocation():
    penup()
    setpos(randint(-400,400), randint(-400,400))
    pendown()

#uma função para desenhar uma estrela de um tamanho específico
def drawStar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    penup()

#isso desenha um fundo azul escuro
bgcolor("MidnightBlue")

#desenha 30 estrelas brancas (tamanhos/posições aleatórias)
for star in range(30):
    moveToRandomLocation()
    drawStar(randint(5,25), "White")

hideturtle()
done()
