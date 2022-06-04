from random import *

print(10*'>', 'NOMES PARA ANIMAIS DE ESTIMAÇÃO', 10*'<')
print(10*'=')

executa = True
lista = ['Totó', 'Snoop', 'Lessie', 'Nina', 'Luna', 'Nino', 'Mel', 'Pretinho', 'Lupe', 'Princesa', 'Luigi']

print('''Serviço de escolha de nome para animais de estimação
-------------------
OPÇÃO:
      a-me dê um nome
      b-me dê mais de um nome
      c-adicione um nome para a lista
      d-imprimir a lista
      e-remove um nome da lista
      f-sair
''')

while executa == True:
    menu = input('Escolha uma opção da lista: ').lower()
    if menu == 'a':
        print(f'Você deve chamar seu animal de estimação de {choice(lista)}')

    elif menu == 'b':
        print(f'Você deve chamar seus animais de estimação de {choice(lista)}, {choice(lista)}, {choice(lista)}, {choice(lista)}')

    elif menu == 'c':
        addNome = input('Adicione um nome para a lista: ')
        if addNome not in lista:
            lista.append(addNome)
        else:
            print('O nome já está na lista')

    elif menu == 'd':
        print(lista)

    elif menu == 'e':
        nomeDel = input('Escolha o nome que será removido: ')
        if nomeDel in lista:
            lista.remove(nomeDel)
        else:
            print('O nome não está na lista!')

    elif menu == 'f':
        executa = False

    else:
        print('ERROR! Escolha uma opção válida!')
        
        
        
