email=False
correo=input("Ingrese direccion de email: ")
print ("El correo es: " + correo)
for i in correo:
    if(i=="@"):
        email=True
if email:
    print ("El email es correcto")
else:
    print("El email es incorrecto")

