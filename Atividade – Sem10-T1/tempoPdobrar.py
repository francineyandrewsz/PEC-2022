'''Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de uma poupança. Mostre
em quantos anos o valor acumulado será o dobro do valor inicial. Por exemplo:
R$100,00 rendendo 8% ao ano irá
dobrar em 10 anos.
Início R$ 100.00
1 ano R$ 108.00
2 anos R$ 116.64
3 anos R$ 125.97
4 anos R$ 136.05
5 anos R$ 146.93
6 anos R$ 158.69
7 anos R$ 171.38
8 anos R$ 185.09
9 anos R$ 199.90
10 anos R$ 215.89

R$100,00 rendendo 10% ao ano
irá dobrar em 8 anos.
Início R$ 100.00
1 ano R$ 110.00
2 anos R$ 121.00
3 anos R$ 133.10
4 anos R$ 146.41
5 anos R$ 161.05
6 anos R$ 177.16
7 anos R$ 194.87
8 anos R$ 214.36

R$200,00 rendendo 15% ao ano
irá dobrar em 5 anos.
Início R$ 100.00
1 ano R$ 230.00
2 anos R$ 264.50
3 anos R$ 304.17
4 anos R$ 349.80
5 anos R$ 402.27

Dica: use repetição com teste no início
'''
deposito = float(input())
taxa = float(input())
juros = taxa / 100
tempo = 0
poup = 0

while poup < deposito * 2:
    tempo += 1
    poup = deposito * (1 + juros) ** tempo

print(tempo)
