salario_presidente=int(input("Introduce el salario del presdidente: "))
print ("Salario presidente es: " + str(salario_presidente))

salario_director=int(input("Introduce el salario del director: "))
print ("Salario director es: " + str(salario_director))

salario_jefe_area=int(input("Introduce el salario del jefe de area: "))
print ("Salario jefe area es: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario del administrativo: "))
print ("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("todo funciona correctamente")
else:
    print("algo falla en esta empresa")