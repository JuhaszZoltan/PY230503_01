from module import *

dolgozok:list[Dolgozo] = []
sorok = open('berek2020.txt', 'r', encoding='utf-8').readlines()
for sor in sorok[1:]: dolgozok.append(Dolgozo(sor))

print(f'összesen {len(dolgozok)} ember dolgozik ezen a helyen')

# összegzés
# pl.:összes kifizetés
osszeg:int = 0
for dolgozo in dolgozok:
    osszeg += dolgozo.ber
print(f'a cég összesen {osszeg} HUF fizetést utal ki')
# -> átlag
#pl.: átlagbér
atlag:float = osszeg / len(dolgozok)
print(f'átlagbér: {round(atlag, 2)} HUF')
# pl 2.: átlagosan egy dolgozó hány éve dolgozik a cégnél
ossz_ev:int = 0
for dolgozo in dolgozok:
    ossz_ev += (2020 - dolgozo.belepes)
atlag_ev:float = ossz_ev / len(dolgozok)
print(f'átlag {round(atlag_ev, 2)} éve dolgozik itt valaki átlagosan')

# megszámlálás
# pl.: hányan doldoznak az 'értékesítés' részlegen?
dolgozok_szama:int = 0
for dolgozo in dolgozok:
    if dolgozo.reszleg == 'értékesítés':
        dolgozok_szama += 1
print(f'értékesítés részlegen dolgozók száma: {dolgozok_szama}')
# -> arány
# pl.: a dolgozók hány %-a dolgozik az értékesítésen?
szazalek:float = dolgozok_szama / len(dolgozok) * 100
print(f'a dolgozók {round(szazalek, 2)}%-a dolgozik az értékesítésen')

# pl. összegzés + megszámlálás + eldöntés: nők átlagbére
nok_osszbere:int = 0
nok_szama:int = 0
for dolgozo in dolgozok:
    if dolgozo.nem == False:
        nok_osszbere += dolgozo.ber
        nok_szama += 1
nok_atlagbere:float = nok_osszbere / nok_szama
print(f'nők átlagbére: {round(nok_atlagbere, 2)} HUF')

# minimum / maximum
# pl.: kinek a legmagasabb a fizetése?
maxindex:int = 0
for index in range(1, len(dolgozok)):
    if dolgozok[index].ber > dolgozok[maxindex].ber:
        maxindex = index
print(f'a legmagasabb fizetés:')
print(f'\tnév: {dolgozok[maxindex].nev}')
print(f'\trészleg: {dolgozok[maxindex].reszleg}')
print(f'\tfizetés: {dolgozok[maxindex].ber} HUF')

# minimum + kiválogatás
# ki/kik dolgoznak a cégnél a legrégebb?
minindex = 0
for index in range(1, len(dolgozok)):
    if dolgozok[index].belepes < dolgozok[minindex].belepes:
        minindex = index
oreg_dolgozok_nevei:list[str] = []
for dolgozo in dolgozok:
    if dolgozo.belepes == dolgozok[minindex].belepes:
        oreg_dolgozok_nevei.append(dolgozo.nev)
print('öreg dolgozók:')
for od in oreg_dolgozok_nevei:
    print(f'\t- {od}')

# eldöntés
# pl while.: dolgozik-e 'Balogh' vezetéknevű ennél a cégnél?
index:int = 0
while index < len(dolgozok) and not dolgozok[index].nev.startswith('Balogh'):
    index += 1
if index < len(dolgozok):
    print('VAN Balogh')
else: print('NINCS Balogh')

# pl for+break.: dolgozik-e 'Juhász' vezetéknevű ennél a cégnél?
for dolgozo in dolgozok:
    if dolgozo.nev.startswith("Juhász"):
        print('VAN Juhász')
        break
else: print('NINCS Juhász')

# keresés
#pl: bekérünk egy nevet -> ha van, kiírjuk a fizetését
# na nincs, kiírjuk, hogy 'nincs ilyen dolgozó
keresett_nev:str = input('írj be egy nevet: ')
for dolgozo in dolgozok:
    if dolgozo.nev == keresett_nev:
        print(f'{keresett_nev} fizetése: {dolgozo.ber} HUF')
        break
else: print(f'nincs {keresett_nev} evű dolgozó')

#kiválogatás
burzsujok:list[Dolgozo] = []
for dolgozo in dolgozok:
    if dolgozo.ber >= 450000:
        burzsujok.append(dolgozo)
for b in burzsujok:
    print(f'\t- {b.nev}: {b.ber} HUF')