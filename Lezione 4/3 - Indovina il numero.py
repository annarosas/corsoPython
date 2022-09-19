# coding=utf-8
# Gioco > Indovina il numero
print('Giochiamo a "Indovina il numero". Inserisci un numero da uno a 10')
while True:
    line = int(input(''))
    if line == 3:
        break
    elif line > 3:
        print('Numero troppo grande')
    else:
        print('Numero troppo piccolo')


print('Hai vinto!')
