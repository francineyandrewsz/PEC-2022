'''Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano)
 e escreva qual delas é a mais recente.'''

dia1 = int(input().strip())
mes1 = int(input().strip())
ano1 = int(input().strip())
dia2 = int(input().strip())
mes2 = int(input().strip())
ano2 = int(input().strip())

recente = (f'{dia1}/{mes1}/{ano1}')
recente2 = (f'{dia2}/{mes2}/{ano2}')

if dia1 > dia2 or mes1 > mes2 or ano1 >ano2:
    print(recente)
else:
    print(recente2)
