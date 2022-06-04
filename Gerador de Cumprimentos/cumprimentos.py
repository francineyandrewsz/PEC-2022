from random import *

print("Gerador de Cumprimentos")
print("-----------------------")

adjetivos = ["maravilhoso", "acima da média", "excelente"]
hobbies = ["andar de bicicleta", "programar", "fazer chá"]

nome = input("Qual é seu nome?: ")
print("Aqui está o seu cumprimento", nome, ":")

#obtém um item aleatório de ambas as listas e adiciona-os ao cumprimento
print(nome, "você é", choice(adjetivos), "em", choice(hobbies))
print("De nada!")

