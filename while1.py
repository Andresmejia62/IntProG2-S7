"Leer una palabra difernete a fin y convertirla en mayuscula"

palabra = input("Dime una palabra: ")
while palabra.lower() != "fin": 
    print(f"{palabra.upper()} tiene {len(palabra)} letras")
    palabra = input("Dime una palabra: ")
else: 
    print("Adios")