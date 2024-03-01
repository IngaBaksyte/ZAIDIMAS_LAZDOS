import math, random

# f-ja, kuri išvalo failą nuo senų duomenų
def valytiFaila():
    with open('reg.txt', 'w') as f:
        pass

# f-ja rašo info į failą reg.txt
def rasytiIFaila(txt):
    with open('reg.txt', 'a', encoding='utf-8') as f:
        f.write(txt + '\n')

# parenka linksnį
def linksniuoti(kiek):
    if kiek == 1:
        tekstas = 'lazdelę'
    else:
        tekstas = 'lazdeles'
    return tekstas


valytiFaila()

zaid1 = input('Įveskite pirmo žaidėjo vardą:  ')
zaid2 = input('Įveskite antro žaidėjo vardą:  ')
rasytiIFaila(f'Žaidėjų vardai: {zaid1} ir {zaid2}\n')
zaid = [zaid1, zaid2]
zaidSk = 0 # žaidimų skaičius

# pradedam žaidimą
while True:
    zaidSk += 1
    rasytiIFaila(f'{zaidSk} ŽAIDIMAS\n')
    lazdSk = int(input('Pasirinkite pradinį lazdelių skaičių: '))
    rasytiIFaila(f'Lazdelių pasirinktas skaičius yra {lazdSk}.')
    random.shuffle(zaid) # atsitiktiniu būdu paskirstom žaidėjų eiliškumą
    i = 0 # pradeda 0 pozicijoje esantis Žaidėjas
    print(f'Žaidimą pradeda {zaid[i]}.')
    rasytiIFaila(f'Žaidimą pradeda {zaid[i]}.')
    #veiksmuSk = 0
    while lazdSk > 0:
        kiek = int(input(f'Kiek lazdelių ima {zaid[i]}? 1, 2 ar 3? '))
        if 1 <= kiek <= 3:
            if lazdSk >= kiek:
                lazdSk -= kiek
                print(f'{zaid[i]} paėmė {kiek} {linksniuoti(kiek)}. Liko {lazdSk}')
                rasytiIFaila(f'{zaid[i]} paima {kiek} {linksniuoti(kiek)}. Lieka {lazdSk}')
                #veiksmuSk += 1
                # žaidėjo keitimas
                #i = round((1 - (-1)**(veiksmuSk))/2) # sekos 0, 1, 0, 1, 0, 1, ... n-to elemento paėmimas
                # arba toks žaidėjų keitimas:
                zaid.reverse()
            else:
                print(f'Tiek lazdelių paimti negalima. Likę tik {lazdSk}')
        else:
            print('Neteisingas lazdelių kiekis :( Kartokite...')

    print(f'\nŽaidimą laimėjo {zaid[i]}!\n')
    rasytiIFaila(f'\nŽaidimą laimėjo {zaid[i]}.\n')
    ats = input('Ar žaisite dar?(T/N) ')
    if ats != 'T' and ats != 't':
        print ('Viso gero...')
        rasytiIFaila(f'\nĮ užklausą „Ar žaisite dar“ pasirinko „Ne“.')
        break

rasytiIFaila(f'Žaidimą žaidė {zaidSk} kartą(us).')