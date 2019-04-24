print("Verificacion de acceso")

edad_usuario=int(input("Ingresatu edad por favor: "))
if edad_usuario<18:
    print("no puede pasar")
elif edad_usuario >= 100:
    print("Edad incorrecta")
else:
    print("puede pasar")

print("El programa a finalizado")
