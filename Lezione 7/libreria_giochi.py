# libreria per minigiochi in python

# MORRA CINESE
# giocatore contro computer
def morra_singolo_giocatore():
    # importo il modul "random" per usare la funzione builtin radint() che genera dei numeri interi random
    from random import randint
    giocatore = input('Scegli sasso, carta o forbice   ')
    while True:
        if giocatore != 'carta' and giocatore != 'sasso' and giocatore != 'forbice':
            print('Errore, digita una delle seguenti parole: "sasso", "carta", "forbice" ')
            giocatore = input('scegli sasso, carta o forbice ').lower()
        else:
            break
    print('Hai scelto', giocatore)
    # utilizzo radint() per cambiare in maniera randomica il valore delle variabile computer in un range da 0 a 2
    computer = randint(0, 2)
    # definisco il tipo di giocata da associare ad ogni numero
    if computer == 0:
        computer = 'sasso'
    elif computer == 1:
        computer = 'forbice'
    else:
        computer = 'carta'
    print('Il tuo avversario ha scelto ', computer)

    if giocatore == 'carta' and computer == 'sasso' or giocatore == 'forbice' and computer == 'carta' or giocatore == 'sasso' and computer == 'forbice':
        print(' Complimenti, hai vinto! ')
    elif giocatore == 'carta' and computer == 'carta' or giocatore == 'forbice' and computer == 'forbice' or giocatore == 'sasso' and computer == 'sasso':
        print(' è un pareggio!')
    else:
        print(' Mi spiace, hai perso!')
    replay = input('Nuova partita? (digita SI o NO').upper()
    if replay == 'SI':
        morra_singolo_giocatore()
    else:
        print('Ciao, ci vediamo alla prossima!')


# giocatore contro giocatore
def morra_due_giocatori():
    nome_giocatore1 = input('GIOCATORE 1: Inserisci il tuo nome per favore  ')
    nome_giocatore2 = input('GIOCATORE 2: Inserisci il tuo nome per favore  ')
    # definisco una funzione nested per poter effettuare il replay del gioco senza chiedere nuovamente i nomi ai giocatori

    def gioco():
        print('Ciao ', nome_giocatore1.upper(), ' e ', nome_giocatore2.upper(), 'iniziamo il gioco!')
        print(nome_giocatore1.upper(), ' inizi tu:')
        giocatore1 = input('scegli sasso, carta o forbice ')

        while True:
            if giocatore1 != 'carta' and giocatore1 != 'sasso' and giocatore1 != 'forbice':
                print('errore, digita una delle seguenti parole: "sasso", "carta", "forbice" ')
                giocatore1 = input('scegli sasso, carta o forbice ')
                # in caso di errore, far ripartire il ciclo da capo
            else:
                break
        print('hai scelto', giocatore1)
        print(nome_giocatore2.upper(), ' tocca a te:')
        giocatore2 = input('scegli sasso, carta o forbice  ')

        while True:
            if giocatore2 != 'carta' and giocatore2 != 'sasso' and giocatore2 != 'forbice':
                print('errore, digita una delle seguenti parole: "sasso", "carta", "forbice" ')
                giocatore2 = input('scegli sasso, carta o forbice ')
                # in caso di errore, far ripartire il ciclo da capo
            else:
                break
            print('hai scelto', giocatore2)

        if giocatore1 == 'carta' and giocatore2 == 'sasso' or giocatore1 == 'forbice' and giocatore2 == 'carta' or giocatore1 == 'sasso' and giocatore2 == 'forbice':
            print('Ha vinto', nome_giocatore1.upper())
        elif giocatore1 == 'carta' and giocatore2 == 'carta' or giocatore1 == 'forbice' and giocatore2 == 'forbice' or giocatore1 == 'sasso' and giocatore2 == 'sasso':
            print(' è un pareggio!')
        else:
            print('Ha vinto', nome_giocatore2.upper())
        replay = input('Nuova partita? (digita SI o NO)').upper()
        if replay == 'SI':
            gioco()
        else:
            print('Ciao, ci vediamo alla prossima!')
    return gioco()


