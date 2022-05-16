from random import *

jogando = True
score = 0

#imprima as 3 portas e as instruções do jogo
print('''
Porta da Fortuna!
========

Existe um super prêmio atrás de uma destas 3 portas!
Advinhe qual é a porta certa para ganhar o prêmio!
  _____   _____   _____
 |     | |     | |     |
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |    o| |    o| |    o|
 |     | |     | |     |
 |_____| |_____| |_____|
 ''')

#deixe o jogador fazer 3 tentativas
while jogando == True:
    print('\nEscolha uma porta(1, 2, ou 3):')

    #pegue a porta escolhida e armazene com um número (int)
    portaEscolhida = int(input())

    #escolha aleatoriamente a porta que esconde o prêmio (entre 1 e 3)
    portaCerta = randint(1, 3)

    #mostre ao jogador qual a porta ele escolheu e qual era a porta certa
    print(f'A porta escolhida foi {portaEscolhida}')
    print(f'A porta certa é {portaCerta}')

    #o jogador ganha se o número da porta escolhida e o da porta certa forem o mesmo, se ele perder zera a pontuação
    if portaEscolhida == portaCerta:
        print('Parabéns!')
        score = score + 1
    else:
        score = 0
        print('Que pena!')

    print(f'Sua pontuação é {score}')

    #pergunte ao jogador se ele quer continuar jogando
    print('\nVocê quer jogar de novo? (s/n)')
    resposta = input().lower()[0]

    #termina o jogo se o jogador digitar 'n'
    if resposta == 'n':
        jogando = False

print('Obrigado por jogar')
print(f'Sua pontuação final é de {score}')
