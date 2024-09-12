def calcular_area_cuadrado(lado):
    return lado ** 2


lado = float(input("Ingresa la longitud del lado del cuadrado: "))
area = calcular_area_cuadrado(lado)

print(f"El área del cuadrado es: {area}")
