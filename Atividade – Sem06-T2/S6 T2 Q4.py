car = input().strip().upper()
if 'A' <= car <= 'Z':
    print(True)
elif car in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
    print(True)
else:
    print(False)
    
