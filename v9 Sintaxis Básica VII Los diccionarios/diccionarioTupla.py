mitupla=["Ecuador","Colombia","Fracia","Cuba"]

midiccionario={mitupla[0]:"Quito", mitupla[1]:"Bogota", mitupla[2]:"Paris", mitupla[3]:"La Habana"}

print(midiccionario)

#En un diccionario a una clave se le puede asignar un tupla  por ejemplo

midiccionario1={"Pais":"Ecuador", "Poblacion":14500780,"Provincias":["Carchi","Imbabura","Pichincha", "Loja", "Manabi"]}


print(midiccionario1)

#guardar un diccionario en otro diccionario

midiccionario2={"Pais":"Ecuador", "Poblacion":14500780,"Provincias":{"Carchi":"Tulcan","Imbabura":"Ibarra","Pichincha":"Quito", "Loja":"Loja", "Manabi":"Portoviejo"}}

print(midiccionario2)
#imprimir las claves

print("Imprimiendo las claves")

print(midiccionario2.keys())

#imprimiendo los valores

print("Imprimiendo los valores")

print(midiccionario2.values())

#imprimir ell total de elementos

print("imprimiendo total de elemetos del diccionario")
print(len(midiccionario2))

