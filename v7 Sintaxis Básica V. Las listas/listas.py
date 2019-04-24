milista=["Carlos","Diana","Catalina","Carmen","Sofia","Diana"]
#print (milista[0])

#print (milista[-3]) #empieza a contar desde el final con -1

#print(milista[0:2]) #porcion de lista 
#print(milista[:2]) #porcion de lista desde la poscion 0 al posicion 2 excluyete

#print(milista[1:3]) #porcion de lista: incluye posicion 1 excluye posicion 3

#print(milista[1:]) #porcion de lista: incluye posicion 1 hasta el final de la lista

#milista.append("Vladimir") #agrega un elemento al final de la lista

#milista.insert(2,"Canela") # esto hace que se agregue en una posicion especifica es decir en la 2

#milista.extend(["Copito","Galli","Ramon"]) #agregar varios elemntos a la lista

#print(milista.index("Diana")) # imprime el indice del valor de la lista
#print(milista.index("Diana")) #si hay valores iguales en la lista imprime el primero en encontrar

#print("Sandro" in milista) #para preguntar si el elemento existe en la lista; devuelve true o false

#print(milista[:]) #imprime todos los elementos de la lista


#la potencia de python es que se puede almacenar diferentes tipos de datos en una unica lista

milista2=["Carlos", "Molina",69,1.67,True]

def sumarPeso(peso,estatura):
    resultado=peso+estatura
    return resultado

#print(sumarPeso(milista2[2],milista2[3]))

milista2.extend(["Diana","Vladimir","Copito"])



#milista2.remove("Vladimir") #remover o eliminar un elemnto 

#milista2.pop() #elimina el ultimo elemento de la lista


milista3=milista+milista2 #Esto permite concatenar listas en una tercer lista

#print(milista3[:])#imprimimos la 3 lista

milista=milista*3 #esta instruccion repite la lista 3 veces

print(milista[:])

