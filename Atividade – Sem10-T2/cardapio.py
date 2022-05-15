'''O cardápio de uma casa de lanches, especializada em sanduíches, é dado abaixo.
CÓDIGO     PRODUTO       PREÇO (R$)
 H         Hamburger      5.50
 C        Cheeseburger    6.80
 M        Misto Quente    4.50
 A           Americano    7.00
 Q        Queijo Prato    4.00
 X        PARA TOTAL DA CONTA
 Escreva um programa que leia o código de vários itens comprados por um freguês e acumule o total da
compra. Ao finalizar com “X”, exiba o total a pagar.
Observações:
• Se for informada uma opção que não está no menu deve mostrar a mensagem “Opção
inválida.”.
• Enquanto o código não for 'X' o programa deve continuar lendo os itens.
Dica: Use upper() para ignorar a diferenças entre maiúscula e minúsculas; Use [0] para garantir que
apenas o primeiro caractere digitado seja considerado. Por exemplo:
         codigo = input('Código: ').upper()[0]     '''

codigo = '5'
saldo = 0

while codigo != 'X':
    print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')

    codigo = input().upper().strip()

    if codigo == 'H':
        saldo += 5.50

    elif codigo == 'C':
        saldo += 6.80

    elif codigo == 'M':
        saldo += 4.50

    elif codigo == 'A':
        saldo += 7.00

    elif codigo == 'Q':
        saldo += 4.00


print(f'{saldo:.2f}')






