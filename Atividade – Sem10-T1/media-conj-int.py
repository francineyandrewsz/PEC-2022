'''Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo
número 0 (zero). Ao final, o programa deve mostrar a média aritmética de todos os números lidos
(excluindo o zero).
Dica: use repetição com teste no final'''

qtd = soma = 0
loop = True
while loop:
    n = int(input())
    if n == 0:
       loop = False
    else:
        soma += n
        qtd += 1

if qtd != 0:
    print(f'{soma/qtd:.2f}')








