# genero il file
import shutil
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
file.close()


# creo una cartella
cartella = 'esercitazione'
if not os.path.isdir(cartella):
    os.makedirs(cartella)

# creo un file dentro la cartella e scelgo il formato del file
file = 'esempio' + '.doc'
file_path = cartella + '/' +file
with open(os.path.join(cartella, file), 'w') as temp_file:
    temp_file.write('ciao')

# Cancello la cartella ma su windows ho problema di permessi


os.remove(str(file_path))
os.stat(cartella)
os.remove(cartella)

os.chmod('C:/Users/sviluppo/Documents/CorsoPython/corsoPython/lezione 9/esercitazione', stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
shutil.rmtree('C:/Users/sviluppo/Documents/CorsoPython/corsoPython/lezione 9/esercitazione', ignore_errors=True)
# Se provo a rimuovere la cartella ottengo PermissionError: [WinError 5] Accesso negato: 'esercitazione'