import random
import string

#versione 1 - Lascio sceglie all'utente il numero di caratteri

print('Benvenuto nel generatore di password')

lunghezza = int(input('Quanti caratteri?'))

numeri = string.digits
simboli = string.punctuation
minuscole = string.ascii_lowercase
maiuscole = string.ascii_uppercase

combinazione = maiuscole + numeri + simboli + minuscole

combinazione_random = random.sample(combinazione, lunghezza)
password = ''.join(combinazione_random)

print(password)

#versione 2 - due opzioni semplice e complessa
print('Benvenuto nel generatore di password')

tipo = input('Vuoi una password semplice o complessa? digita "S" per semplice e "C pe complessa').lower()
semplice = 8
complessa = 20
numeri = string.digits
simboli = string.punctuation
minuscole = string.ascii_lowercase
maiuscole = string.ascii_uppercase
combinazione = maiuscole + numeri + minuscole
if tipo == 's':
    combinazione_random = random.sample(combinazione, semplice)
    password = ''.join(combinazione_random)
    print(password)
else:
    combinazione = combinazione + simboli
    combinazione_random = random.sample(combinazione, complessa)
    password = ''.join(combinazione_random)
    print(password)






