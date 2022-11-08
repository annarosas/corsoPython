# 2) Scrivere un programma Python che:
# A. Richiede all’utente di inserire un numero N compreso tra 5 e 15
# B. Richiede all’utente di inserire N elementi e li memorizza in una lista L
# C. Creare una copia L2 della lista L
# D. Modificare il valore di N/3 elementi della lista L2 scelti in modo casuale
# con valori casuali tra 0 e 100 (valutare se opportuno scrivere una
# funzione)
# E. Stampare (utilizzare la funzione sommaElem(list) dell’esercizio 1) il
# valore della lista L e della lista L2


import random

while True:
    try:
        lista_lenght = int(input("Inserisci un numero tra compreso tra 1 e 15: "))
    except ValueError:
        print("Errore. Per favore inserisci un numero tra compreso tra 1 e 15")
        continue
    if lista_lenght >= 1 and lista_lenght <= 15:
        print(f'Hai inserito: {lista_lenght}')
        break
    else:
        print('Errore, il numero inserito non è compreso tra 1 e 15')

# definisco la variabile lista e la lunghezza
listaElementi = []

# creo contatore elementi (mi serve solo per il testo che mostrerò all'utente)
n = 1

# Messaggio all'utente
print(f'Creiamo una lista di {lista_lenght} numeri')

# Richiesta elementi lista all'utente
while(True):
    try:
        elementi= int(input(f'Inserisci l\'elemento {n} di {lista_lenght}. '))
        listaElementi.append(elementi)
        print(listaElementi)
        n = n + 1
    except:
        print('Errore. Inserisci un numero intero')
    else:
        # raggiunto il numero di elementi desiderati stampo la lista finale
        if len(listaElementi) == lista_lenght - 1:
            print('Ci sei quasi! Manca l\'ultimo')
        elif len(listaElementi) == lista_lenght:
            print(f'Complimenti hai creato una lista di {lista_lenght} elementi.')
            break

# creo una copia della lista
# non modifca quella originale
copiaLista = listaElementi[:]

# genero una lista di 3 numeri casuali da 0 a 100
numbers = random.sample(range(0, 100), 3)

# creo un indica random per modificare tre elementi casuali della lista dell'utente
# ovviamente non uso numbers perchè rischierei di andare fuori indice, infatti utilizzo lista_lenght per definire il range
replace = random.sample(range(0, lista_lenght), 3)


# creo la funzione che sostituisce elementi casuali della lista con 3 numeri casuali da 1 a 100
def replaceList(nomeLista, numeri, replace):
    i = 0
    for n in numeri:
        nomeLista[replace[i]] = numeri[i]
        i = i + 1


replaceList(copiaLista, numbers, replace)

print(f'La tua lista è stata modificata. \n'
      f'Questa è la lista che hai creato {listaElementi} \n'
      f'Questa è la sua copia modificata {copiaLista} \n'
      f'Sono stati modificati gi elementi con questo indice {replace} \n'
      f'al loro posto sono stai inseriti questi elementi {numbers}. \n'
      f'La somma di questa nuova lista è: ')

print(sum(copiaLista))











