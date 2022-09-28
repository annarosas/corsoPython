# coding=utf-8
from datetime import date, datetime

oggi = (date.today()).strftime("%d/%m/%Y")
oggi_datetime = (datetime.strptime(oggi, '%d/%m/%Y')).year

data_nascita = input("Inserisci la tua data di nascita(gg/mm/AAAA): ")
dtnascita = (datetime.strptime(data_nascita, '%d/%m/%Y')).year

anni =  oggi_datetime - dtnascita
if anni>= 18:
    print('Dalla tua nascita sono passati', anni, 'anni. Sei maggiorenne')
else:
    print('Dalla tua nascita sono passati', anni, 'anni. Sei minorenne')
