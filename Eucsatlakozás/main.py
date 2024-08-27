#2. feladat-------------------------------------------------------------------
'''
f = open("EUcsatlakozas (1).txt" , encoding="utf8")
lista = []
for sor in f:
  lista.append(sor.strip().split(';'))
'''
with open("EUcsatlakozas (1).txt" , encoding="utf8") as f:
     lista = [sor.strip().split(';') for sor in f]
#3. feladat--------------------------------------------------------------------
print(f"3. feladat: EU tagállamainak száma: {len(lista)} db")
#4. feladat---------------------------------------------------------------------
'''
szamlalo = 0
for sor in lista:
  if sor[1][0:4] == "2007":
    szamlalo = szamlalo + 1
print(f"4. feladat: 2007-ben {szamlalo} orszag csatlakozott")
'''

csatlakozas_2007 = [sor for sor in lista if sor[1][0:4] == "2007"]
print(f"4. feladat: 2007-ben {len(csatlakozas_2007)} ország csatlakozott.")

#5. feladat-----------------------------------------------------------------------
for sor in lista:
  if sor[0] == "Magyarország":
    a_csatlakozas_datum = sor[1]
print(f"5. feladat: Magyarország csatlakozásának dátuma: {a_csatlakozas_datum}")
#6. feladat------------------------------------------------------------------------
szamlalo = 0
for sor in lista:
  if sor[1][5:7] == "05":
    szamlalo = szamlalo + 1

if szamlalo > 0:
  print("6. feladat: Májusban volt csatlakozás!")
else:
  print("6. feladat: Nem volt csatlakozás májusban")
#7. feladat-----------------------------------------------------------------------
utoljara = lista[0][1]
orszag = lista[0][0]
for sor in lista:
   if sor[1] > utoljara:
     utoljara = sor[1]
     orszag = sor[0]
print("7. feladat: Legutoljára csatlakozott ország:", orszag)
#8. feladat--------------------------------------------------------------------------

