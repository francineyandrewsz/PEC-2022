car = input().lower()
if car in ('a','e', 'i', 'o', 'u'):
    print('vogal')
elif car in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
    print('consoante')
elif car in ('0','1','2','3','4','5','6','7','8','9'):
    print('número')
else:
    print('símbolo')
