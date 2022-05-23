'''Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Escreva um programa
que leia um número e determine se ele é ou não primo.'''

n = int(input().strip())
count = 0
i = 0

while i <= n or count < 2:
    i = i + 1
    x = n % i
    if x == 0:
        count += 1
if count <= 2:
    print(True)
else:
    print(False)
    
