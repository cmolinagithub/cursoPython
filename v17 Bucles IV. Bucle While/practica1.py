
import math
'''
i=1
while i<=10:
    print("Ejecucion" + str(i))
    i=i+1
print("Termino ejecucion")
'''
#funcionamiento de while

## Programa para verificar la edad

'''
edad=int(input("Ingrese su edad por favor:   "))

while edad<5 or edad>100:
    print("Edad incorrecta, vuelva a intentar")
    edad=int(input("Ingrese su edad por favor:   "))
print ("Gracias por colaborar. Puedes pasar")
print ("Edad del aspirante "+ str(edad))

'''

##ejemplo de raiz cuadrada

print ("Programa de cálculo de raíz cuadrad ")

numero=int(input("Introduzca un # por favor:  "))

intentos=0

while numero<0:
    print("No existe raiz cuadrado de negativos")
    if intentos==2:
        print("has consuminod demasiados intentos. Fin programa")
        break
    numero=int(input("Introduzca un # por favor:  "))

    if numero<0:
        intentos=intentos+1
if intentos<2:
    solucion=math.sqrt(numero)
    print ("La raiz cuadrad de: " +str(numero)+ " es "+ str(solucion))







