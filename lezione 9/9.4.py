# genero il file
import os
import stat

with open('nuovofile.txt', 'w') as file:
    file.write('Giuseppe GARIBALDI' + '\n' +
               'Lucrezia BORGIA' + '\n' +
               'Giulio CESARE' + '\n' +
               'Muzio SCEVOLA' + '\n' +
               'Alessandro MAGNO' + '\n' +
               'Dante ALIGHIERI' + '\n' +
               'Marco POLO' + '\n' +
               'Carlo MAGNO' + '\n' +
               'RE Umberto Primo' + '\n' +
               'RE Carlo Alberto')

# definisco varibile e leggo il file
file = open('nuovofile.txt', 'r')

# leggo le righe
riga1 = file.readline()
riga2 = file.readline()
riga3 = file.readline()

# verifico che le righe non siano vuote
if len(riga1) > 0 and len(riga2) > 0 and len(riga3) > 0:
    # stampo
    print(riga1, riga2, riga3)

# chiudo il file

file.close()

# creo una cartella
cartella = 'esercitazione'
if not os.path.isdir(cartella):
    os.makedirs(cartella)

# Cancello la cartella ma su windows ho problema di permessi
# PermissionError: [WinError 5] Accesso negato: 'esercitazione'

os.remove(cartella)