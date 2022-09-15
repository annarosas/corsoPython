# coding=utf-8
# Controllo età
nome_utente = raw_input('Come ti chiami?')
# Ho notato che premendo INVIO il programma va avanti quindi ho provato il metodo che segue ma mi sembra "sporco"

while not nome_utente:
    nome_utente = raw_input('Come ti chiami?(questo campo è obbligatorio)')

eta_utente = ''

while not eta_utente:
    try:
        eta_utente = int(raw_input('Quanti anni hai?'))
    except:
        print('Errore."Quanti anni hai è un campo numerico ed è obbligatorio"')

print('Ciao ' + nome_utente + ' benvenuto!')
if eta_utente >= 18:
    print('A quanto pare sei maggiorenne')
else:
    print('Wow sei giovane, a quanto pare sei minorenne')