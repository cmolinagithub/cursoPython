print ("Programa de becas del 2017")
distancia_escuela=int(input("Introducela la distancia a la escuela en Km "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos "))
print(numero_hermanos)
salario_familia=int(input("Introduce  salario anual bruto "))

if distancia_escuela>40 and numero_hermanos>2 or salario_familia<=20000:
    print("Tiene derecho a beca")
else:
    print("No tiene derecho a beca")
