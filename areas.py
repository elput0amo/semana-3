base = float(input (f"Cual es la longitud de la base: "))
altura = float(input (f"Cual es la longitud de la altura: "))

def calculate_area(base, altura):
    area = base*altura/2
    return area 
area = calculate_area(base,altura)
print (f"el area es de {area:.2f} metros cuadrados")


