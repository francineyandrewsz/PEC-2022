def percentual(valor, porcentagem):
    return valor *(porcentagem / 100)

p = float(input("Preço: "))
valor_p = float(input("Percentual: "))
p_acres = p + percentual(p, valor_p)
p_desc = p - percentual(p, valor_p)
print(f'R${p} com acréscimo de {valor_p}% fica por R${p_acres}')
print(f'R${p} com desconto de {valor_p}% fica por R${p_desc}')



