
texto = input("Introduce una cadena de texto: ")


a = e = i = o = u = 0

for letra in texto.lower():
    if letra == 'a':
        a += 1
    elif letra == 'e':
        e += 1
    elif letra == 'i':
        i += 1
    elif letra == 'o':
        o += 1
    elif letra == 'u':
        u += 1

print("Cantidad de vocales:")
print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)
