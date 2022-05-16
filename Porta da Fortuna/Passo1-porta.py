from random import *

#imprima as 3 portas e as instruções do jogo
print('''
Porta da Fortuna!
=========

Existe um super prêmio atrás de uma destas 3 portas!
Advinhe qual é a porta certa para ganhar o prêmio!

   _____   _____   _____
  |     | |     | |     |
  |     | |     | |     |
  | [1] | | [2] | | [3] |
  |    O| |    O| |    O|
  |     | |     | |     |
  |_____| |_____| |_____|

''')

#deixe o jogador fazer 3 tentativas
for attempt in range(3):

    print('\nEscolha uma porta (1, 2 ou 3):')
    
    #pegue a escolhida e a armazene com um número inteiro(int)
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)

    #escolha aleatoriamente a porta que esconde o prêmio (entre 1 e 3)
    portaCerta = randint(1,3)

    #mostre ao jogador qual a porta ele escolheu e qual era a porta certa
    print('A porta escolhida foi a', portaEscolhida)
    print('A porta certa é a', portaCerta)

    #o jogador quanha se o número da porta escolhida e o da porta certa forem o mesmo.
    if portaEscolhida == portaCerta:
        print('Parabéns!')
    else:
        print('Que Peninha!')
    
