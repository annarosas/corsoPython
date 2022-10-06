# esercizio carta di credito

from pathlib import Path
from datetime import datetime
# creo un file sul quale registrare le operazioni

# definisco la classe


class Cartacredito:
    def __init__(self, cf, nome, cognome, codice, mese, anno, cvv, credito):
        self.cf = cf
        self.nome = nome
        self.cognome = cognome
        self.codice = codice
        self.mese = mese
        self.anno = anno
        self.cvv = cvv
        self.credito = credito
# metodo per stampare le info
    
    def info_carta(self):
        return f'CF Intestatario:{self.cf} Nome Intestatario:{self.nome} Cognome Intestatario:{self.cognome} ' \
               f'Codice carta:{self.codice} Mese scadenza:{self.mese} Anno scadenza:{self.anno} CVV:{self.cvv}'
# metodo credito carta
    
    def credito(self):
        return f'{self.credito}'

# metodo prelievo
    def prelievo(self, cifra_prelievo = float(0)):
        try:
            if cifra_prelievo <= self.credito:
                with open('saldo.txt', 'w') as file_s:
                    file_s.write(f'{self.credito - cifra_prelievo}')
                    file_s.close()
                return f'Prelievo eseguito.Il tuo credito residuo è di: {self.credito - cifra_prelievo} Euro'
            else:
                raise Exception(f'credito non sufficiente')
        except Exception:
            return f'Errore.credito non sufficiente.Il credito disponibile è di {self.credito}' \
                   f' EURO. Effettua un versamento.'
# metodo versamento
    
    def versamento(self, cifra_versamento = float(0)):
        try:
            if cifra_versamento > 0:
                self.credito = self.credito + cifra_versamento
                with open('saldo.txt', 'w') as file_s:
                    file_s.write(f'{self.credito}')
                    file_s.close()
                return f'Versamento effettutato.credito totale disponibile: {self.credito} EURO '
            else:
                raise Exception(f'Errore')
        except Exception:
            return f'Errore.La cifra del versamento è troppo bassa.'


# definisco l'oggetto carta 1

carta1 = Cartacredito('svrnrs87l63g273s', 'Anna', 'Savarino', '3020 345 1234 4335', '09', '2024', '000', 0)


# chiedo all'utente che operazione vuole svolgere
operazione = input('Che operazione vuoi effettuare? "P" = Prelievo, "V" = Versamento,'
                   ' "S" = Saldo, "OP" = ultime 10 operazioni"').upper()
if operazione:
    # leggo il saldo attuale dal file saldo
    saldo_file = Path('saldo.txt')
    # se non sono stati effettuati versamenti il file potrbbe non essere sidponibile
    # verifico che il file esista
    if saldo_file.is_file():
        with open("saldo.txt") as file:
            saldo_attuale = file.read()
            saldo_attuale_int = float(saldo_attuale)
            carta1 = Cartacredito('svrnrs87l63g273s', 'Anna', 'Savarino', '3020 345 1234 4335',
                                  '09', '2024', '000', saldo_attuale_int)

            file.close()

# inizializzo il file operazioni
    with open('operazioni_bancomat.txt', 'a') as file:
        file.write('')
        file.close()


# gestisco gli esiti delle operazioni
# conservo la data odierna in una variabile, mi servirà per registrare le operazioni
data = datetime.today()
if operazione == 'P':

    cifra_prelievo = float(input('Quanto vuoi prelevare?'))
    print(carta1.prelievo(cifra_prelievo))
    with open('operazioni_bancomat.txt', 'a') as file:
        file.write(f'Data: {data} | OPERAZIONE:Prelievo | Cifra prelevata {cifra_prelievo}  \n')
    file.close()


elif operazione == 'V':
    cifra_versamento = float(input('Quanto vuoi versare?'))
    print(carta1.versamento(cifra_versamento))
    with open('operazioni_bancomat.txt', 'a') as file:
        file.write(f'Data: {data} | OPERAZIONE:Versamento | Cifra versata {cifra_versamento}  \n')
    file.close()

elif operazione == 'S':
    saldo_file = Path('saldo.txt')
    if saldo_file.is_file():
        with open("saldo.txt", 'r') as file:
            saldo_aggiornato = file.read()
            print(f'Il tuo saldo è di {saldo_aggiornato} euro')
    else:
        print('Saldo non disponibile')
elif operazione == 'OP':
    n_operazioni = 10
    with open("operazioni_bancomat.txt") as file:
        last_n_lines = file.readlines()[-n_operazioni:]
        print(last_n_lines)
        file.close()
else:
    print('Funzione errata o non disponibile. Arrivederci.')
