a=10
b=20
c=0

print(a>b) #false
print(c<b) #true
print(a>b and c<b) #false
print(a>b or c<b) #true
print(not a) #false w przypadku gdy zmienna ma wartość zero, (), {}, [] to domyslnie jest false, jesli niezerowa to true

print("Wynik dzialania ptrojny warunek" \
      "to:", a > b and b > c or a > c)
            # false and true 
            # false or true            wynik finalny = true

