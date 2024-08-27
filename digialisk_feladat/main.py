#https://youtu.be/Wy9zlSlwoVQ
import random

valasz = int(input("Milyen műveletet szeretne gyakorolni?\n 1. Összeadás\n 2. Kivonás\n 3. Szorzás\nVálasztás (1-3): "))
ok = 0
db = 0
while ok < 5:
    db += 1
    a = random.randint(1,10)
    b = random.randint(1,10)
    if valasz == 1:
        d = a + b
        print("{} + {} = ?".format(a, b))
    elif valasz == 2:
        d = a - b
        print("{} - {} = ?".format(a, b))
    else:
        valasz == 3
        d = a * b
        print("{} * {} = ?".format(a, b))
    c = int(input("Megoldás: "))
    if c == d:
        ok += 1
        print("Helyes!")
    else:
        print("Hibás!")

print("Gratulálunk!")
print("Sikerült {} helyes műveletet elvégezni {} próbálkozásból.".format(ok, db))
        
        