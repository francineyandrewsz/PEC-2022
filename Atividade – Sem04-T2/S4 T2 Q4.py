def min_p_h(q_min):
    h = q_min // 60
    m = q_min % 60
    return f'{h}h{m}min'
minutos = int(input('Quantidade de minutos: '))
horas = min_p_h(minutos)
print(f'{minutos} minutos são equivalentes a {horas}')



