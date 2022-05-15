'''Escreva um programa Python que apresente o menu de opções abaixo:

O programa deve ler a opção do usuário e exibir, para cada opção, a respectiva mensagem:

OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM

1 - Olá. Como vai?
2 - Vamos estudar mais.
3 - Meus Parabéns!
0 - Fim de serviço.

Se for informada uma opção que não está no menu deve mostrar a mensagem “Opção inválida.”.
Enquanto a opção for diferente de 0 (zero) deve-se continuar apresentando as opções. Obs: use como
estrutura de repetição com teste no final e como estrutura condicional múltipla escolha.'''

while True:
    #Escolha uma das opções.
    print('''OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')
    #Informe a opção.
    opcao = int(input())
    if opcao == 1:
        print('1 - Olá. Como vai?')
    elif opcao == 2:
        print('2 - Vamos estudar mais.')
    elif opcao == 3:
        print('3 - Meus Parabéns!')
    elif opcao == 0:
        print('0 - Fim de serviço.')
        break
    else:
        print('Opção inválida.')

