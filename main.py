import random

# #Zad1
liczby = []
for i in range(50):
    a = random.randrange(100)
    liczby.append(a)
podzielne = [x for x in liczby if x % 4 == 0]
print(podzielne)
podzielnestr = []
for y in podzielne:
    s = str(y)
    podzielnestr.append(s)
plik = open("plik1.txt", "wb")
for x in podzielnestr:
    z = str(x)
    plik.write(z)
plik.close()

#Zad2

#Zad3

plik = open("plik2.txt", "wb")
plik.write("Kilka")
plik.write("\n")
plik.write("linijek")
plik.write("\n")
plik.write("tekstu.")
plik.close()

with open("plik2.txt") as tekst:
    print(tekst.read())
    tekst.close()

