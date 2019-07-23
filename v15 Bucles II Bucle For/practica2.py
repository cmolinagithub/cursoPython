contador=0
miEmail=input("Ingrese su correo:  ")

print("Correo es:  "+miEmail)

for i in miEmail:
    if(i=="@" or i=="."):
        contador=contador+1
if contador==2:
    print("Email es correcto")
else:
    print("Email es incorrecto")