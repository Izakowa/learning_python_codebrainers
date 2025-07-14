#typ niemutowalny, niezmienny - krotka

krt = (1,2,3,4,5)

# krt[2] = 10 nie da się zmienić drugiego elementu na liście na 10

#czy da się modyfikować krotkę?

lst = list(krt)

#modyfikacja listy
lst[2]= 10

#przypisz (przekonwertuj z powrotem na krotke)
krt = tuple(lst)

print("Krotka to:", krt, "oraz typ:", type(krt)) #typowa konkatenacja
print("Krotka to: {} oraz typ: {}".format(krt,type(krt))) #funkcja do formatowania tekstu
print("Krotka to: {0} oraz typ: {1}".format(krt,type(krt))) #funkcja do formatowania tekstu
print(f"Krotka to: {krt} oraz typ: {type(krt)}")    # f-string

