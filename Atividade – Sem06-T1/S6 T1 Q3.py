'''Escolha uma cor:
[V] Verde
[A] Amarelo
[E] Vermelho
'''
cor = str(input()).strip().upper()
if cor == 'V':
    print('Siga')
elif cor == 'A':
    print('Atenção')
elif cor == 'E':
    print('Pare')
