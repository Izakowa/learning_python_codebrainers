interable_element = "codebrainers"

for elements in interable_element:
    pass #dzięki temu nie ma błędu, a można zostawić przestrzeń na później

for element in interable_element:
    print("Litera:", element)

interable_element = 'Codebrainers'
i = 0
for element in interable_element:
    print("Litera:", element, "przebieg pętli", i)
    i += 1

# interable_element = ("C", "o", "d", "e") - inny przykład

# interable_element = 'Codebrainers'
interable_element = ("C", "o", "d", "e")

# interable_element = list(interable_element)
i = 0
for element in interable_element:
    print("Litera:", element, "przebieg pętli", i)
    i += 1
    if element == 'o':
        print("o!")

# Drukowanie wartosci slownika 
iterable_dictionary = {"C": 1, "o": 2, "d": 3, "e": 4}
for element in iterable_dictionary:
    print("Element slownika", iterable_dictionary[element])
for key, value in iterable_dictionary.items():
    print("Klucz", key, "Wartosc", value)

    # interable_element = 'Codebrainers'
interable_element = ("C", "o", "d", "e")
# interable_element = list(interable_element)
i = 0
for element in interable_element:
    print("Litera:", element, "przebieg pętli", i)
    i += 1
    if element == 'o':
        print("o!")
# Drukowanie wartosci slownika 
iterable_dictionary = {"C": 1, "o": 2, "d": 3, "e": 4}
for element in iterable_dictionary:
    print("Element slownika", iterable_dictionary[element])
for key, value in iterable_dictionary.items():
    print("Klucz", key, "Wartosc", value)
# To jest przyklad kiedy mamy zbyt wiele nawiasow i mamy krotke, ktora 
# moze to nam wplynac na dalszy przebieg programu 
for key, value in iterable_dictionary.items():
    print(type(("Klucz", key, "Wartosc", value)))

    # zawsze bedzie iterowac od 0!
for x in range(10):
    print("iks =", x)

# https://docs.python.org/3.13/library/functions.html#func-range

# zawsze bedzie iterowac od 0!
# range(start, stop, step)
for x in range(50, 61, 2):
    print("iks =", x)

# Iterujemy od konkretnego indeksu
example_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for l in range(5, 10, 1):
    print(example_lst[l])

# Można ewentualnie zastosowac wycinek
print(example_lst[5:10:1])