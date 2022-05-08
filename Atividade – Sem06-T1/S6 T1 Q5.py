n1 = float(input().strip())
n2 = float(input().strip())
n3 = float(input().strip())
soma = n1 + n2 +n3
media = soma / 3
if n3 > 8:
    media += 1
    if media > 10:
        media = 10

print(f'{media:.2f}')
    
