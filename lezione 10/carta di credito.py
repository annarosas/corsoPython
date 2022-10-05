# esercizio carta di credito
# definisco la classe
class CartaCredito:
    def __init__(self, cf, nome, cognome, codice, mese, anno, cvv ):
        self.cf = cf
        self.nome = nome
        self.cognome = cognome
        self.codice = codice
        self.mese = mese
        self.anno = anno
        self.cvv = cvv
# metodo per stampare le info
    def infoCarta(self):
        return f'CF Intestatario:{self.cf} Nome Intestatario:{self.nome} Cognome Intestatario:{self.cognome} Codice carta:{self.codice} Mese scadenza:{self.mese} Anno scadenza:{self.anno} CVV:{self.cvv}'
# metodo credito carta
    def Credito(self, credito_disponibile=0):
        self.credito_disponibile=credito_disponibile

        return f'Credito disponibile:{self.credito_disponibile}'
#metodo prelievo
    def prelievo(self, cifraPrelievo='0'):
        try:
            if(cifraPrelievo<=self.credito_disponibile):
                return f'Prelievo eseguito.Il tuo credito residuo è di: {self.credito_disponibile - cifraPrelievo} Euro'
            else:
                raise Exception(f'Credito non sufficiente')
        except Exception:
           return f'Errore.Credito non sufficiente.Il credito disponibile è di {self.credito_disponibile} EURO'
#metodo versamento
    def versamento(self, cifraVersamento='0'):
        try:
            if (cifraVersamento > 0):
                self.credito_disponibile = self.credito_disponibile + cifraVersamento
                return f'Versamento effettutato.Credito totale disponibile: {self.credito_disponibile} EURO '
            else:
                raise Exception(f'Errore')
        except Exception:
            return f'Errore.La cifra del versamento è troppo bassa.'





# definisco l'oggetto carta 1
carta1 = CartaCredito('svrnrs87l63g273s', 'Anna', 'Savarino', '3020 345 1234 4335', '09', '2024', '000')
# definisco il credito disponibile per l'oggetto carta 1
carta1_credito = carta1.Credito(1000)
# stampo le info di carta 1
print(carta1.infoCarta())

# chiedo all'utente che operazione vuole svolgere
operazione = input('Che operazione vuoi effettuare? Digita "P" per prelievo, digita "V" per versamento, "S" per stampare il saldo').upper()
# gestisco gli esiti delle operazioni
if (operazione == 'P'):
    cifraPrelievo = int(input('Quanto vuoi prelevare?'))
    print(carta1.prelievo(cifraPrelievo))

elif (operazione == 'V'):
    cifraVersamento = int(input('Quanto vuoi versare?'))
    print(carta1.versamento(cifraVersamento))

elif (operazione == 'S'):
    print(carta1_credito)


