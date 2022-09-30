# coding=utf-8
# Tabellina
numero = ''

while not numero:
    numero = int(input('Inserisci un numero per vedere la tabellina'))
    for y in range(10):
        print(numero * (y+1))
