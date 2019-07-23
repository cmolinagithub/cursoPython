for i in range(5):
    print (f"Valor de la variable {i}")

# Mas argumentos para range

for i in range(5,59,3):
    print(f"EL valor de la variable {i}")

# mas ejemplos 
valido =False
email="cmolinabastidas.gmail.com"

for i in range(len(email)):

    if email[i]=="@":
        valido=True

if valido:
    print("Email es correcto")

else:
    print("El email es incorrecto")
