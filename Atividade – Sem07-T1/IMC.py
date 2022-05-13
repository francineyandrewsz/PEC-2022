'''O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso
ideal. O IMC é determinado pela divisão da massa do indivíduo pelo quadrado de sua altura, em que a massa está
em quilogramas e a altura em metros. Escreva um programa que leia a massa (o peso) e a altura de uma pessoa e
calcula o IMC de uma pessoa, e depois, mostra uma das seguintes mensagens:

    IMC           Classificação
    <18,5         Abaixo do peso
    <25           Peso normal
    <30            Sobrepeso
    <35             Obeso leve
    <40            Obeso moderado
    >=40           Obeso mórbido
'''
#Informe o peso e altura da pessoa
peso = float(input())
altura = float(input())
#calcule o IMC
imc = peso / (altura ** 2)
#imprime o peso
print(f'{imc:.0f}')
#Indique a classificação da pessoa
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso normal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 35:
    print('Obeso leve')
elif 35 <= imc < 40:
    print('Obeso moderado')
elif imc >= 40:
    print('Obeso mórbido')

    
