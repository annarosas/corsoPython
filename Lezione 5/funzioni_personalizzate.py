# dizionari
eta = {
    'anna': 2,
    'maria': 15,
    'carlo': 24,
    'rebecca': 50
}

# ordino per chiave
for key in sorted(eta):
    print("%s: %s" % (key, eta[key]))

# ordino per valore
eta_val_ordered = sorted(eta.items(), key=lambda x: x[1])
for i in eta_val_ordered:
	print(i[0], i[1])

# verificare se elemento esiste nel dizionario

if 'anna' in eta:
    print('presente')
else:
    print('assente')

# estrarre in base alla chiave
chiavi = {key: eta[key] for key in eta.keys()
          &{'carlo','maria'}
          }
print(str(chiavi))
# estrarre in base ai valori
valori = {key: eta[key] for key in eta.keys()
          &{'carlo','maria'}
          }

# Estrarre chiavi, Estrarre valori
chiavi = list(eta.keys())
valori = list(eta.values())
print(chiavi)
print(valori)

#aggiungere
eta['lia'] = '70'
print(eta)

# eliminare
del eta['carlo']
print(eta)

