gravedades = {
   "Mercurio" : -3.7,
   "Venus" : -8.87,
    "Tierra": -9.81,
    "Marte" : -3.71,
    "Jupiter": -28.79,
    "Saturno" :-10.44,
    "Urano" : -8.87,
    "Neptuno": -11.15,
    

}
#esta es la base de datos de los planetas y sus gravedades

planeta = input ("En que planeta estas: ")
gravedad = gravedades [planeta]
print (f" La gravedad de tu planeta {gravedad} ")
altura1 = float (input ("Altura inicial (m): " ))
time = float(input ("En que segundo lo quieres (en el instante inicial es 0): "))
#estos son los valores que va a introducir el usuario

altura_variable = altura1+gravedad*time
#esta va a ser la altura que se va a imprimir 

print (f"Tu altura en el segundo {time} es de {altura_variable:.2f} m/s")
