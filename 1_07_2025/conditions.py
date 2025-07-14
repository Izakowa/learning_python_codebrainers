punkty = 72 
if punkty < 10:
    print("Mniej niz 10, nie zdales")
elif punkty < 20:
    print("Mniej niz 20, nie zdales")
elif punkty < 70:
    print("Mniej niz 70 nie zdales")
elif punkty <= 72:
    print("Zdales!")
else:
    print("Punkty poza skalą")

punkty = 60
# print("passed") if punkty >= 60 else print("not passed")
punkty = 40
# x = "Zdałeś" if punkty >= 50 and punkty < 100 else "Nie zdałeś"
x = "PASSED!" if punkty >= 50 and punkty < 100 else "FAILED"
print(x)
# Standardowa implementacja 
x = ""
if punkty >= 50 and punkty < 100:
    x = "PASSED"
else:
    x = "FAILED"