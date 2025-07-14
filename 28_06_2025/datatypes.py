true = 10
false = 20
print(true, false)

a = 2 == 2
b = 5 < 10

a = (2 == 2)
b = (5 < 10)
print("Czy 2 jest rowne 2?", a)
print("Czy 5 jest mniejsze od 10?", b)

print("typ zmiennej a, to typ:", type(a), "typ zmiennej b, to typ:", type(b))

print("Typ zmiennej a, to typ:", type(a), "typ zmiennej b, to typ:", type(b))
new_value = str(a)
print("Typ zmiennej new_value, to typ:", type(new_value))
old_list = ['a','b','c']
new_str = str(old_list)
print(new_str, "i jest to typu", type(new_str), "dlugosc", len(new_str))