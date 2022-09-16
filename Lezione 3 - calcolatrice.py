# coding=utf-8
numero_1 = int(input('Inserisci il primo numero: '))
numero_2 = int(input('Inserisci il secondo numero: '))

operazione = input('Che tipo di operazione vuoi svolgere?Digita:'
                   '+ per addizione'
                   '- per sottrazione'
                   '* per moltiplicazione'
                   '/ per divisione')


def addizione():
    print(numero_1+numero_2)


def sottrazione():
    print(numero_1-numero_2)


def moltiplicazione():
    print(numero_1*numero_2)


def divisione():
    print(numero_1/numero_2)


if operazione == '+':
    print('il risultato è: ')
    addizione()

elif operazione == '-':
    print('il risultato è: ')
    sottrazione()

elif operazione == '*':
    print('il risultato è: ')
    moltiplicazione()

elif operazione == '/':
    print('il risultato è: ')
    divisione()
