# 2) Scrivere un programma Python che:
# A. Richiede all’utente di inserire un numero N compreso tra 5 e 15
# B. Richiede all’utente di inserire N elementi e li memorizza in una lista L
# C. Creare una copia L2 della lista L
# D. Modificare il valore di N/3 elementi della lista L2 scelti in modo casuale
# con valori casuali tra 0 e 100 (valutare se opportuno scrivere una
# funzione)
# E. Stampare (utilizzare la funzione sommaElem(list) dell’esercizio 1) il
# valore della lista L e della lista L2


numero = 0

while True:
    try:
        numero = int(input("Inserisci un numero tra compreso tra 1 e 5: "))
    except ValueError:
        print("Errore. Per favore inserisci un numero tra compreso tra 1 e 5")
        continue
    if numero >= 1 and numero <= 5:
        print(f'Hai inserito: {numero}')
        break
    else:
        print('Errore, il numero inserito non è compreso tra 1 e 5')