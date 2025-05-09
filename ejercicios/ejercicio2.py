M = int(input("Introduce un número entero positivo M: "))
producto = 1
contador = 0
numero = 2

while contador < M:
    producto *= numero
    contador += 1
    numero += 2

print("El producto de los primeros", M, "números pares es:", producto)
