'''nome = input("Qual seu nome? ")

#imprima cada caracter do seu nome
for char in nome:
    print(char)'''

#uma lista de letras para criptografar
alfabeto = "abcdefghijklmnopqrstuvwyz"

#capture a mensagem do usuário
mensagem = input("Por favor, entre com a mensagem a ser criptografada: ").lower()

#esta variável armazenará a mensagem criptografada
mensagemCriptografada = ""

#capture a chave secreta
chave = input("Por favor, entre a chave: ")
#Esta ação é necessária porque o programa não lê o valor da chave como o número
chave = int(chave)

#percorra cada caracter na mensagem
for char in mensagem:
    if char in alfabeto:

        #encontre a posição de caracter em alfabeto
        #por exemplo, 'a' está na posição 0, 'e' está na posição 4, etc.
        posicao = alfabeto.find(char)

        #some a chave secreta para encontrar a posição do caracter criptografado
        #% 26 significa 'volte para 0 quando você atingir 26
        novaPosicao = (posicao + chave) % 26

        #acrescente a letra descriptografada à mensagem
        #a letra criptografada está em alfabeto na novaPosicao
        mensagemCriptografada = mensagemCriptografada + alfabeto[novaPosicao]

    else:

        #alguns caracteres (por exemplo '£', '?') não estão alfabeto,
        #então simplesmente adicione a letra criptografada à mensagem
        mensagemCriptografada = mensagemCriptografada + char

print("Sua mensagem criptografada é:", mensagemCriptografada)

    
