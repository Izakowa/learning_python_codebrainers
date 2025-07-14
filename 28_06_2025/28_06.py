# Biorąc pod uwagę ciąg o nieparzystej długości większej niż 7,
# zwróć łańcuch złożony z trzech środkowych znaków danego ciągu:
# Dane wejściowe:
#     `str1 = "Datatypes"`
# Oczekiwany wynik:\
#     `aty`

word = "mialkocja"
print(word)
print(word[3:6])

word2 = "mialkkocjacjacja"
print(word2)
srodek = int(len(word2)/2)
print(srodek)
print(word2[srodek-1:srodek+2])

# Biorąc pod uwagę ciąg o nieparzystej długości większej niż 7,
# zwróć łańcuch złożony z trzech środkowych znaków danego ciągu:
# Dane wejściowe:
#     `str1 = "Datatypes"`
# Oczekiwany wynik:
#     `aty`
print("Propozycja 1")
str1 = 'Datatypes'
print(str1[3:6])
str2 = "DatatypesDatat1"
# Licze dlugosc ciagu
middle = int(len(str2)/2)
print(middle)
print(str2[(middle - 1):middle + 2])
# str[5:9] -> str[5:8] - bo 9 nie jest brana pod uwage

# Biorąc pod uwagę ciąg o nieparzystej długości większej niż 7,
# zwróć łańcuch złożony z trzech środkowych znaków danego ciągu:
# Dane wejściowe:
#     `str1 = "Datatypes"`
# Oczekiwany wynik:
#     `aty`
print("Propozycja 1")
str1 = 'Datatypes'
print(str1[3:6])
str2 = "DatatypesDatat1"
# Licze dlugosc ciagu
middle = int(len(str2)/2)
print(middle)
print(str2[(middle - 1):middle + 2])
# str[5:9] -> str[5:8] - bo 9 nie jest brana pod uwage 
 
print(str1.isalpha())
print(str2.isalpha())