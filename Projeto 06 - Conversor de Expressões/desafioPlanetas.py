distancia_Planetas = {
    "mercúrio" : 57910000,
     "vênus" : 108200000,
     " terra" : 149600000,
     "marte" : 227940000,
     "júpiter" : 778330000,
     "saturno" : 1429400000,
     "urano" : 2870990000,
     "netuno" : 4504300000,
     "plutão" : 5922000000
}

#obtém o planeta para a saber a distância
planeta = input('Digite um planeta: ').lower()
distancia = distancia_Planetas[planeta]

#imprime a frase
print(planeta, 'está a', distancia, 'km do Sol')




