print("Asignatura optativas Anio 2017")
print("Asignaturas optativas: Infomatica - Software - Usabilidad")
asignatura=input("Ingrese materia escogida")
try:
    if asignatura in("Informatica", "Software", "Usabilidad"):
        print("Asignatura escogida "+asignatura)
    else:
        print("Asignatura no corresponde")
except ValueError:
    print("Indeterminado")