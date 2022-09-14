# coding=utf-8
# Controllo età
nome_utente = raw_input('Come ti chiami?')
try:
    eta_utente = int(raw_input('Quanti anni hai?'))
except:
    print('Errore. Il campo età è numerico')
    nome_utente = raw_input('Come ti chiami?')
    if eta_utente >= 18:
        print('A quanto pare sei maggiorenne')
    else:
        print('Wow sei giovane, a quanto pare sei minorenne')


else:
    print('Ciao ' + nome_utente + ' benvenuto!')
    if eta_utente >= 18:
        print('A quanto pare sei maggiorenne')
    else:
        print('Wow sei giovane, a quanto pare sei minorenne')

#controllo password
password = 'Password_sicura'
insert_password = raw_input('Per favore digita la password di accesso')

if password == insert_password:
    print('Benvenuto!')
else:
    print('Password non corretta')

#esercizio3 - controllo età e password
nome_utente = raw_input('Come ti chiami?')
try:
    eta_utente = int(raw_input('Quanti anni hai?'))
except:
    print('Errore. Il campo età è numerico')

password = 'Password_sicura'
if eta_utente >= 18:
    print('Ciao ' + nome_utente + ' benvenuto!')
    insert_password = raw_input('Per favore digita la password di accesso')
    if password == insert_password:
        print('Benvenuto!')
    else:
        print('Password non corretta')
else:
    print('Purtroppo non puoi accedere, sei minorenne. Torna tra qualche anno! :)')



#calcolo paga con e senza straordinari
ore_lavorate = int(raw_input('Quante ore hai lavorato?'))
paga_oraria = 10
if ore_lavorate > 40:
    print('A quanto pare hai fatto degli straordinari')
    ore_straordinario = ore_lavorate - 40
    paga_totale = ore_straordinario*15 + 40*paga_oraria
    print('In totale hai guadagnato ' + str(paga_totale) + ' euro')
elif ore_lavorate < 40:
    print('A quanto pare hai saltato qualche ora')
    print('In totale hai guadagnato ' + str(ore_lavorate*paga_oraria) + ' euro')
elif ore_lavorate == 40:
    print('Non hai fatto straordinari')
    print('In totale hai guadagnato ') + str(ore_lavorate*paga_oraria) + (' euro')