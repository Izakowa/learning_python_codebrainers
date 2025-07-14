words = "Miał miał i miał miał"
words_lenght = len(words) #przyjmuje sekwencje (np. listy też, inne elementy)
print("długość napisu:", words_lenght)

print(words[2])
print(words[20])

print(words[0]) # pierwszy znak  
print(words[52]) # ostatni znak dlugosc napisu - 1
print(words[-1]) # ostatni znak 
print(words[-2]) # przedostatni znak

print(words[0]) # pierwszy znak  
print(words[52]) # ostatni znak dlugosc napisu - 1
print(words[-1]) # ostatni znak 
print(words[-2]) # przedostatni znak
print(words[0:6]) # od 0 do 6 (nie wliczajac 6)
print(words[2:6]) 
print(words[10:20])
print(words[15:]) # od 15 do konca 
print(words[0:-1:2])

start = 0 
end = 30
step = 2
print(words[start:end:step])

