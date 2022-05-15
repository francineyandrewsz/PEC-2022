'''Escreva um programa que, para um número indeterminado de pessoas:

a. leia a idade de cada pessoa, sendo que a leitura da idade 0 (zero) indica o fim dos dados (flag)
e não deve ser considerada;
b. calcule e escreva o número de pessoas;
c. calcule e escreva a idade média do grupo;
d. calcule e escreva a menor idade e a maior idade.'''

qtd = soma = maior = menor = 0
idade_pessoa = int(input())
while idade_pessoa != 0:
    qtd += 1
    soma += idade_pessoa
    idade_pessoa = int(input())
    if qtd == 1:
        maior = menor = idade_pessoa
    else:
        if idade_pessoa != 0:
            if idade_pessoa > maior:
                maior = idade_pessoa
            if idade_pessoa <  menor:
                menor = idade_pessoa

if soma != 0:
    media = soma / qtd
    print(f'{qtd}')
    print(f'{media:.2f}')
    print(f'{menor}')
    print(f'{maior}')





