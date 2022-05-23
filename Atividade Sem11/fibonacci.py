'''A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, na qual, cada termo
subsequente corresponde à soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). Escreva um programa que
leia um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci. O valor lido para n
sempre será maior ou igual a 2.'''

n = int(input().strip())
cont = 3
t1 = 0
t2 = 1
print(f'{t1}, {t2}', end='')
while cont <= n:
    t3 = t1 + t2
    print(f', {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
    
