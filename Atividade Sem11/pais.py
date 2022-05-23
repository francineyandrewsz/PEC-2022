'''Dado um país A, com taxa de natalidade de 2% ao ano, e um país B com uma taxa de natalidade de 3%
ano. Sabe-se que, atualmente, o país A tem população maior que o país B. Faça um programa que leia a
população de cada país e imprima o tempo necessário para que a população do país B ultrapasse a
população do país A.'''

def montante(b, i, t):
    return b*(i**t)

def troca(a, b):
    if b > a:
        aux = b
        b = a 
        a = aux
    return a,b
        
if __name__ == "__main__":
    a = int(input().strip())
    b = int(input().strip())
    a,b = troca(a,b)
    t = 0
    while(montante(b, 1.03, t) < montante(a, 1.02, t)):
        t += 1

    print(t)
    
