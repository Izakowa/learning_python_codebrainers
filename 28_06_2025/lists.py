number_list = []
print(number_list)

number_list = [                                ]
print("Zawartosc listy: ", number_list)
print("Dlugosci listy: ", len(number_list))

number_list1 = [0, 1, 2, 3, 4, 5555]
print("Zawartosc listy: ", number_list1)
print("Dlugosci listy: ", len(number_list1))
print("Wycinek listy:", number_list1[-1])
print("Wycinek listy:", number_list1[2:3:2])

# Wypełnijcie te listy odpowiednimi wartościami
number_list2 = []
string_list = [] 
# Wydrujkujemy zawartość listy

number_list2 = [1, 2, 3, 4]
string_list = ["a", "b", "c", "d"]

new_list = number_list2 + string_list
print(new_list)
[1, 2, 3, 4, 'a', 'b', 'c', 'd']

# Wydrujkujemy zawartość listy
new_list = number_list2 + string_list
print("Nowa lista:", new_list)
# Dodawanie elementow do listy 
new_list.append(6)
print("Nowa lista:", new_list)

# Dodawanie elementow do listy 
new_list.append(6)
print("Nowa lista:", new_list)
# Pobieranie indeksu danego elementu z listy:
print(new_list.index('d'))
# Sciagamy element z listy:
new_list.pop()
print("Nowa lista:", new_list)

# Szukanie elementu w liscie:
print("a" in new_list)  # Dwie wartosci True lub False

unsorted_list = [1412, 15241, 122 ,1 ,2 ,3 ,5551 ,112314, 6251541]
unsorted_list.sort()
print("Posortowana lista:", unsorted_list)

# Odwracanie listy:
unsorted_list.reverse()
print("Odwrocona lista:", unsorted_list)

#mixed_list = [1, 'b', 'c', 3.14, "tekst", 14124141, 111, 222, "131231"]
mixed_list = [1, 3.14, 14124141, 111, 222]
mixed_list.sort(reverse=True)
print("Posortowana lista mieszana:", mixed_list)

# Sortowanie kodow ascii 
ascii_list = ['a', 'A', 'b', 'B', 'c', 'C']
ascii_list.sort()
print("Posortowana lista ascii:", ascii_list)

# Listy zagnieżdzone
macierz = [[1,2,3],[4,5,6],[7,8,9]]

# Listy zagnieżdzone
macierz = [[1,2,3],
           [4,5,6],
           [7,8,9]]
print(len(macierz))  # Dlugosc macierzy = 3
print(len(macierz[0]))  # Dlugosc wycinka macierzy = 3
# Odwracamy liste zagniezdzona
macierz[-1].reverse()
print("Odwrócona macierz:", macierz)