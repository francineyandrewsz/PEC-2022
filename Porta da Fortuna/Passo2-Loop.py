from random import *

#o usuário muda esta variável para terminar o jogo
jogando = True

score = 0

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
 |    o| |    o| |    o|
 |     | |     | |     |
 |_____| |_____| |_____|
 ''')

#repetir, enquanto a variável 'jogando' estiver com valor 'True' (Verdadeiro)
while jogando == True:

    print("\nEscolha uma porta (1, 2, ou 3):")

    #pegue a porta escolhida e a armazene como um número inteiro(int)
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)

    #escolha aleatoriamente a porta que esconde o prêmio(entre 1 e 3)

    portaCerta = randint(1,3)

    #mostre ao jogador qual a porta ele escolheu e qual a era a porta certa

    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)

    #o jogador ganha se o número da porta escolhida e o da porta certa forem os mesmos
    if portaEscolhida == portaCerta:
        print("Parabéns!")
        score = score + 1
    else:
        print("Que peninha!")

    print("Sua pontuação é", score)

    #pergunte ao jogador se ele quer continuar jogando

    print("\nVocê quer jogar de novo?(s/n)")
    resposta = input()
    #terminar o jogo se o jogador digitar 'n'
    if resposta == 'n':
        jogando = False

print("Obrigado por jogar.")
print("Sua pontuação final é de", score)
