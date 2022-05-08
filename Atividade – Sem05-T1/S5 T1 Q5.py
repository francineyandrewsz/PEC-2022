def valorAvista(v):
    return v * 0.91

def valorEmCinco(v):
    return v / 5

def valorEmDez(v):
    return (v * 1.17) / 10

compra = float(input().strip())
print(f'{valorAvista(compra):.2f}')
print(f'{valorEmCinco(compra):.2f}')
print(f'{valorEmDez(compra):.2f}')
