from turtle import *

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

#vai para uma posição diferente(x=200,y=200)
penup()
setpos(200, 200)
pendown()

#use a função para desenhar uma grande estrela branca
drawStar(50, "White")

hideturtle()
done()
