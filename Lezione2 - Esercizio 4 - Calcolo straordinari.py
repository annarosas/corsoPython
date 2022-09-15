# coding=utf-8
#calcolo paga con e senza straordinari
ore_lavorate = ''
while not ore_lavorate:
    try:
        ore_lavorate = int(raw_input('Quante ore hai lavorato?'))
    except:
        print('ore lavorate è un campo obbligatorio e numerico')
    else:
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