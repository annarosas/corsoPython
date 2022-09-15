# coding=utf-8
# esercizio3 - controllo età e password
nome_utente = raw_input('Come ti chiami?')
try:
    eta_utente = int(raw_input('Quanti anni hai?'))
except:
    print('Errore. Il campo età è numerico')
    eta_utente = int(raw_input('Quanti anni hai?'))

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