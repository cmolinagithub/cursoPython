print("Programa de evaluacion de notas de alumnos")

nota_alumno=input("Introduce la nota del alumno") # por lo genera todo lo introducido por teclado es considerado como un string

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="reprobado"
    return valoracion

print (evaluacion(int(nota_alumno)))