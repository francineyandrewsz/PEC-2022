'''Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. Considere que todos os valores
são diferentes. NÃO use as funções embutidas min() e max().'''

num1 = int(input().strip())
num2 = int(input().strip())
num3 = int(input().strip())
num4 = int(input().strip())
num5 = int(input().strip())

def maior(n1, n2, n3, n4, n5):
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        return n1
    elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        return n2
    elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        return n3
    elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        return n4
    return n5


def menor(n1, n2, n3, n4, n5):
    if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
        return n1
    elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
        return n2
    elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
        return n3
    elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
        return n4
    return n5

print(f'{maior(num1, num2, num3, num4, num5)}')
print(f'{menor(num1, num2, num3, num4, num5)}')
