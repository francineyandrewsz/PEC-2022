'''Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. Você deseja comprar um carro, mas o
preço do carro sobe a taxa de 0,4% ao mês. Escreva um programa que leia o preço de um carro hoje e
calcule em quantos meses, com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o
carro à vista.'''

from math import ceil, log

if __name__ == "__main__":
    p = log(10070)
    c = float(input().strip())
    a = log(c*1.004)
    t = 0.0
    while(10000*(1.007**t) < c *(1.004**t)):
        t += 1

    print(t)
