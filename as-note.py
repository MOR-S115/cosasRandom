# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
asignaturas=["matematica","fisica","lenguaje","quimica","historia"]
notes={}
for asignatura in asignaturas:
    nota=float(input("ingresa la nota que has sacado en " + asignatura +":"))
    notes[asignatura]=nota
if len(asignaturas)==5:
    for asignatura in asignaturas:
        print ("en la asignatura de ",asignatura," obtuviste una puntauacion de:",notes[asignatura])
