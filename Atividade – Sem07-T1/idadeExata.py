dia_atual = int(input().strip())
mes_atual = int(input().strip())
ano_atual = int(input().strip())
dia_nasc = int(input().strip())
mes_nasc = int(input().strip())
ano_nasc = int(input().strip())

idadeExata = ano_atual - ano_nasc
if mes_atual < mes_nasc:
    idadeExata = idadeExata - 1
elif dia_atual < dia_nasc:
    idadeExata = idadeExata - 1
print(idadeExata)
