mitupla=("carlos","diana",3,5.6) #ejemplo de una tupla
print(mitupla) #imprime toda la tupla; la tupla se imprime entre parentesis

#convertir la tupla en Lista

milista=list(mitupla)#imprime una lista, el resultado esta entre corchetes

print(milista)

#convertir una lista en tupla

milista1=["Carchi","Tulcan",245000,5,15,15,"15"] #ejemplo de una lista

print(milista1) #impresion de la lista

mitupla1=tuple(milista1) #la lista se convierte en tupla

print(mitupla1) #se imprime la tupla.

#ver si un elemento se encuentra en la tupla 
print ("Ver si un elemento existe en la tupla")
print(15 in mitupla1)

#contar las veces que aparezca un elemento en una tupla 

print("veces que aparece un elemento en la tupla")

print(mitupla1.count(15))
#longitud de una tupla

print("total de elementos en una tupla")

print(len(mitupla1))

#tuplas unitarias

mitupla2=("carlos",)
print("tuplas unitarias")
print(len(mitupla2))

'''tuplas se las  puede definir sin parentesis
a estas se la conoce como empaquetado de tuplas
'''
print("Empaquetado de tuplas")

mitupla3="Carlos","Molina",69.6,120
print(mitupla3)

#desempaquetado de tuplas o asiganacion en variables

mitupla4=("Carlos Molina", 20, 05,1984)

nombre, dia, mes, agno=mitupla4

print("Datos personales")

print("Nombre:  " +nombre)
print("dia:  " + str(dia))
print("mes:  " + str(mes))
print("anio:  " + str(agno))



