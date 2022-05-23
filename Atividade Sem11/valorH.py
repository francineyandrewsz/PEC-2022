'''Sendo H = 1 + 1/2 + 1/3 + 1/4 + ...+ + 1/n,
escreva um programa para calcular o valor de H. O número n é lido.'''

n = int(input().strip())
h = 0

for i in range(1, n+1):
    h = h + 1/i

print(f'{h:.4f}')


    
