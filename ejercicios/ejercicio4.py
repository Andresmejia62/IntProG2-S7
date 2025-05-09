calif_1= int(input(" introduce la calificación 1: "))
calif_2= int(input(" introduce la calificación 2: "))
calif_3= int(input(" introduce la calificación 3: "))
N = (calif_1, calif_2, calif_3)
suma = 0
for i in N:
    suma += i
promedio = suma / len(N)
print(f"la calificación promedio es: {promedio:.2f}")