palabra = input ("Dime una palabra")

for palabra in iter(input, "fin"):
    print(f"{palabra.capitalize()} tiene {len(palabra)} letras")
else: 
    print("Termino...")