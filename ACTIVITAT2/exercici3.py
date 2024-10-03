a = int(input("Introdueix un número: "))
b =  int(input("Introdueix un altre número: "))

max = a
min = a

if b > max:
    max = b

if b < min:
    min = b

print("Mayor:", max)
print("Menor:", min)