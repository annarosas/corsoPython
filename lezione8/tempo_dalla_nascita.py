from datetime import date, datetime

oggi = (date.today()).strftime("%d/%m/%Y")
oggi_datetime = datetime.strptime(oggi, '%d/%m/%Y')

data_nascita = input("Inserisci la tua data di nascita(gg/mm/AAAA): ")
dtnascita = datetime.strptime(data_nascita, '%d/%m/%Y')

giorni =  oggi_datetime - dtnascita


print('Dalla tua nascita sono passati', giorni)





