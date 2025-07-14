# def suma_mn(number):
#     """
    
#     """

#     suma = 0

#     for i in range(number + 1):
#         suma = suma + i #suma += i  (i - iterator)
#         print("wartosc i= ", i, "suma: ", suma)
#     return suma

# print (suma_mn(3))

def suma_rekurencja(number):
    if number == 0:
        return 0
    print("number= ", number)
    return number + suma_rekurencja(number - 1)

print(suma_rekurencja(3))