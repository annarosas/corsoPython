#importo la libreria_giochi che ho precedentemente creato

import libreria_giochi
print('Benvenuto alla morra cinese. Contro chi vuoi giocare?')

# il giocatore sceglie se giocare contro il computer o contro un avversario
# converto i caratteri in maiuscole (per il case sensitive e poichè non mi interessa "forzare" il giocatore ad usare maiuscole o minuscole)
tipo_gioco = input('Digita "C" per giocare contro il computer, digita "A" se hai un avversario').upper()

if tipo_gioco == 'C':
   print('Hai scelto di giocare contro il computer.')
   libreria_giochi.morra_singolo_giocatore()

elif tipo_gioco == 'A':
   print('Hai scelto di giocare contro un avversario.')
   libreria_giochi.morra_due_giocatori()

