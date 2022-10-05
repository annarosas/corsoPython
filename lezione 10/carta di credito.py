# esercizio carta di credito
import shutil
import os
import stat
# creo un file sul quale registrare le operazioni

# definisco la classe
class CartaCredito:
    def __init__(self, cf, nome, cognome, codice, mese, anno, cvv, credito ):
        self.cf = cf
        self.nome = nome
        self.cognome = cognome
        self.codice = codice
        self.mese = mese
        self.anno = anno
        self.cvv = cvv
        self.credito = credito
# metodo per stampare le info
    def infoCarta(self):
        return f'CF Intestatario:{self.cf} Nome Intestatario:{self.nome} Cognome Intestatario:{self.cognome} Codice carta:{self.codice} Mese scadenza:{self.mese} Anno scadenza:{self.anno} CVV:{self.cvv}'
# metodo credito carta
    def Credito(self):
        return f'Credito disponibile: {self.credito}'

        return f'Credito disponibile:{self.credito}'
#metodo prelievo
    def prelievo(self, cifraPrelievo='0'):
        try:
            if(cifraPrelievo<=self.credito):
                return f'Prelievo eseguito.Il tuo credito residuo è di: {self.credito - cifraPrelievo} Euro'
            else:
                raise Exception(f'Credito non sufficiente')
        except Exception:
           return f'Errore.Credito non sufficiente.Il credito disponibile è di {self.credito} EURO'
#metodo versamento
    def versamento(self, cifraVersamento='0'):
        try:
            if (cifraVersamento > 0):
                self.credito = self.credito + cifraVersamento
                return f'Versamento effettutato.Credito totale disponibile: {self.credito} EURO '
            else:
                raise Exception(f'Errore')
        except Exception:
            return f'Errore.La cifra del versamento è troppo bassa.'





# definisco l'oggetto carta 1
carta1 = CartaCredito('svrnrs87l63g273s', 'Anna', 'Savarino', '3020 345 1234 4335', '09', '2024', '000', 1000)

# stampo le info di carta 1
print(carta1.infoCarta())

# chiedo all'utente che operazione vuole svolgere
operazione = input('Che operazione vuoi effettuare? Digita "P" per prelievo, digita "V" per versamento, "S" per stampare il saldo').upper()
if operazione:
    with open('operazioni_bancomat.txt', 'a') as file:
        file.write(f'operazioni carta {carta1.infoCarta()} + \n')
# gestisco gli esiti delle operazioni
if (operazione == 'P'):
    cifraPrelievo = int(input('Quanto vuoi prelevare?'))
    print(carta1.prelievo(cifraPrelievo))

elif (operazione == 'V'):
    cifraVersamento = int(input('Quanto vuoi versare?'))
    print(carta1.versamento(cifraVersamento))

elif (operazione == 'S'):
    print(carta1.Credito())


