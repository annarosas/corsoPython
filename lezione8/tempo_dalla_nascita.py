# coding=utf-8
from datetime import date, datetime
#
oggi = (date.today()).strftime("%d/%m/%Y")
oggi_datetime = datetime.strptime(oggi, '%d/%m/%Y')

data_nascita = input("Inserisci la tua data di nascita(gg/mm/AAAA): ")
dtnascita = datetime.strptime(data_nascita, '%d/%m/%Y')

giorni = oggi_datetime - dtnascita

# giorni è di tipo datetime.timedelta e stampa il termine day e l'ora
# rimuovo giorno è ora perchè voglio solo il numero di giorni
giorni_string = str(giorni)
giorni_num = ''
for num in giorni_string:
    if num.isdigit():
        giorni_num = giorni_num + num
        giorni_num = giorni_num[:5]






print('Dalla tua nascita sono passati', giorni_num)





