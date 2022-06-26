passwordDictionary = {

        "franciney" : "stronger"
        
    }

print("Programa super secreto")
print("====================")


name = input("Nome : ").lower()
password = input("Senha : ").lower()

#verifique se o nome existe e se a senha está correta
if name in passwordDictionary and password == passwordDictionary[name]:

    #adicione o código aqui

    print("\nBEM-VINDO", name.upper())

else:
    
    print("Acesso negado")
