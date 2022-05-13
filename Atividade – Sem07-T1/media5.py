'''Escreva um programa que leia 5 números inteiros, calcule e mostre a média e escreva os que são maiores que a
média. Considere duas casas decimais.'''

n1 = int(input().strip())
n2 = int(input().strip())
n3 = int(input().strip())
n4 = int(input().strip())
n5 = int(input().strip())

media = (n1 + n2 + n3 + n4 + n5) / 5

print(f'{media:.2f}')

if n1 > media:
    print(f'{n1:.2f}')
if n2 > media:
    print(f'{n2:.2f}')
if n3 > media:
    print(f'{n3:.2f}')
if n4 > media:
    print(f'{n4:.2f}')
if n5 > media:
    print(f'{n5:.2}')
