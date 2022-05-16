'''Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo
número 0 (zero). Ao final, o programa deve mostrar o maior e o menor de todos os números lidos
(excluindo o zero).
Dica: use repetição com teste no final'''

qtd = maior = menor = 0
loop = True
while loop:
    n = int(input())
    qtd += 1
    if n == 0:
        loop = False
        break
    if qtd == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
if maior != 0 or menor != 0:
    print(f'{maior}')
    print(f'{menor}')
