'''Escreva um programa que calcule o fatorial de um número inteiro lido, sabendo-se que:
N ! = 1 x 2 x 3 x ... x N-1 x N
0 ! = 1
'''

def fat(n):
    if (n == 0 or n == 1):
        return 1
    return n * fat(n-1)

if __name__ == "__main__":
    num = int(input().strip())
    print(fat(num))
    
