'''Faça um programa que leia a nota de um aluno, entre zero e dez. Mostre a mensagem “Nota inválida.”
caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. Após informar
uma nota válida, o aluno deve ver seu conceito, segundo a tabela:
Conceito     Nota
  A          >= 8,5.
  B          >= 7,0
  C          >= 5,0
  D          >= 4
  E          >= 0
  '''


while True:
    nota = float(input())
    if 8.5 <= nota <= 10.0:
        print('A')
        break
    elif 7 <= nota < 8.5:
        print('B')
        break
    elif 5 <= nota < 7:
        print('C')
        break
    elif 4 <= nota < 5:
        print('D')
        break
    elif 0 <= nota < 4:
        print('E')
        break
    else:
        print('Nota inválida.')
    


