def area_piso(l, c):
    return l * c
def vol_sala(l, c, a):
    return l * c * a
def area_parede(l, c, a):
    return 2 * a * l + 2 * a * c

if __name__== "__main__":
    altura = int(input())
    comprimento = int(input())
    largura = int(input())
    print(area_piso(largura, comprimento))
    print(vol_sala(largura, comprimento, altura))
    print(area_parede(largura, comprimento, altura))

