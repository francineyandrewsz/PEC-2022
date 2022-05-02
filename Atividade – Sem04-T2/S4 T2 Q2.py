def a_quadrado(lado):
    return lado * lado

def perimetro_q(lado):
    return lado * 4

valor_l = float(input())
print(f'{a_quadrado(valor_l):>10.4f}\n{perimetro_q(valor_l):>10.4f}')



