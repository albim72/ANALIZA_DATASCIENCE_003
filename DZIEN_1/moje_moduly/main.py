# import prosta_funkcja
# import prosta_funkcja as pf
from prosta_funkcja import info

#duplikowanie linii/bloku => CTRL+D
#szybkie komentowanie => CTRL+/

#lista
mixlist= [4,6,3.333,-0.0094,True,0x004,"Lublin","ABC"]
print(mixlist)

liczby = [4,2,7,89,35,2,5,89,53,2]
print(liczby)

print(liczby[5])
print(liczby[2:6])
print(liczby[:5])
print(liczby[3:])

liczby.append(111)
print(liczby)
liczby.insert(4,200)
print(liczby)

#krotka
miasta = ("Kraków","Lublin","Opole","Toruń")
print(miasta)
print(miasta[:2])

lmiasta = list(miasta)
print(type(lmiasta))

lmiasta.append("Zamośc")
miasta = tuple(lmiasta)

print(miasta)

#zbiór
drzewa = {"topola","dąb","sosna","świerk","wiśnia","dąb"}
print(drzewa)

drzewa.add("jesion")
print(drzewa)

#słowniki
osoba = {
    "id":6436,
    "imię":"Tomasz",
    "nazwisko":"Kot",
    "miasto":"Warszawa",
    11:"Felix"

}

print(osoba)
print(osoba["nazwisko"])

print(" użycie funkcji prosta_funkcja() ---->")
komunikat = "wiadomośc 53563S"
print(info(komunikat))
