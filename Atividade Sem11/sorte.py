'''O número da sorte de uma pessoa é calculado somando os dígitos da sua data de nascimento. Escreva um
programa que leia a data de nascimento, digitada no formado ddmmaaaa (um número inteiro com 8
dígitos), e mostre o seu número da sorte. Por exemplo, quem nasceu em 29/04/1989 deve digitar 29041989
e o programa vai calcular que o número da sorte é 42 (2 + 9 + 0 + 4 + 1 + 9 + 8 + 9 = 42).'''

def luckBirthday(data):
    t = len(data)     
    sum = 0
    for i in range(0, t):
        sum += (int(data[i]))
        
    return sum

if __name__ == "__main__":
    birthday = (input().strip())
    print(luckBirthday(birthday))
    
