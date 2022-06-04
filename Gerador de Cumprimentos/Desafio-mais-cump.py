from random import *

print(20*"=", "GERADOR DE CUMPRIMENTOS", 20*"=")

adjetivos = ["horrível", "disastre", "muito bom", "preguiçoso"]
hobbies = ["jogar video games", "andar de patins", "namorar", "Python", "assistir filmes"]

nome = input("Qual é o seu nome?\n")
print(f'Esse é seu cumprimento {nome} :')

print(f'{nome} você é {choice(adjetivos)} em {choice(hobbies)}.')
