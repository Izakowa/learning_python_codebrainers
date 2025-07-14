some_list = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 
             4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]
some_set = set(some_list)

print("Zbior: ", some_set, "a jego typ", type(some_set))

new_list = list(some_set)
print(new_list)

# in --> T/F
# not in --> T/F

x=1 in some_set
y=10 not in some_set

a = {1,2,3}
b = {4,5,6}

#zbiory nie operują +-*/

print(a|b) #dodawania
print(a-b) #odejmowania
print(a&b) #mnożenie (część wspólna)
print(a^b) #dzielenie (część rozłączna)

