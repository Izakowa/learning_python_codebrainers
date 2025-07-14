d = {}
# klucze (key)
# wartosci (value)
# k:v - element słownika (item)

d = {"Imię":"Iza",
     "Nazwisko":"Nowak",
     "Telefon":123456789
     }

print("Slownik",d,"typ",type(d))
print("Slownik klucze",d.keys(), "typ",type(d.keys()))
print("Slownik values",d.values(), "typ",type(d.values()))
print("Slownik items",d.items(), "typ",type(d.items()))

# Wyjmujemy wartosc ze slownika bazujac na kluczu 
example = "imie"
print("Pierwsza wartosc ze slownika", d["imie"])
print("Pierwsza wartosc ze slownika", d[example])