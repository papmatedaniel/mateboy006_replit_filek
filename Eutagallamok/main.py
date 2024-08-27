f = open("EU csatlakozás.txt" ,encoding="utf8")
lista = [ ]
for sor in f:
    lista.append(sor.strip().split(','))
# split pontos vessző mentén darabol, strip eltávolítja a nem látható karaktereket.


print(f"3. feladat: EU tagállamainak száma: {len(lista)} db")



szamlalo = 0
for sor in lista:
    if sor[1][0:4] == "2007":
        szamlalo = szamlalo + 1
print (f"4. feladat: 2007-ben {szamlalo} ország csatlakozott.")



for sor in lista:
    if sor[0] == "Magyarország":
        a_csatlakozas_datum = sor[1] 
        print(f"5. feladat: Magyarország csatlakozásának dátuma: {a_csatlakozas_datum}.")