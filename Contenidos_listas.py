mi_variable1 = 1
mi_variable2 = "Pera"

# yo puedo ir teniendo mis variables así como arriba, 
# o bien puedo agrupar variables en una lista, como a continuación, que pongo dos variables que ya definí antes 
# pero también pueden ser valores directos

mi_lista = [mi_variable1, mi_variable2, 1.2, "limon"]
print(mi_lista[-1], "---", mi_lista[3])

# Las listas se pueden sumar. Supongamos que a mi_lista le quiero sumar la lista siguiente de autos. 

autos = ["auto1", "auto2","auto3"]

resultado = mi_lista + autos
print(resultado) 

# inclusive adentro de una lista
# yo podría contener otra lista (una lista anidada, que la pongo entre corchetes adentro)

persona1 = ["Pedro", "Rodríguez", 4, "Tel 112359"]
persona2 = ["Antonia", "Gómez", 2, "Tel 65997"]
Personas_todas = ["Personas del curso", persona1, persona2]
print(Personas_todas)

# Supongamos que a mi lista de personas se agrego una persona más, pero ya no estoy 
# a tiempo para buscar en mi código la lista y agregarla, o por alguna razón la quiero agregar después. 
# Para eso la agrego a la lista con la función append. De la siguiente manera (primero tengo a la persona3)

persona3 = ["Maia", "Hiese", 30, "tel 112392"]

Personas_todas.append(persona3)
print(Personas_todas)

# las listas son mutables. Esto quiere decir que yo puedo cambiar un elemento. 
# No así como los enteros o los str, que son inmutables. Los diccionarios también son mutables.
# Que pasa si quiero multiplicar un elemento de la lista, x 2? Me lo repite ! 

print(Personas_todas[3]*2)

# También existe la opción de extender una lista. Es decir, armar una lista que se llame, 
# por ejemplo, empleados, y ponerle un .extend y agregarle por ejemplo dos listas. De esta manera. 
# genero una lista vacía por ejemplo: 

print("-----------")

empleados = []
empleados.extend([persona1, persona2]) 
print(empleados)

# Otra cosa interesante. supongamos que tengo una persona que tiene dos nombres. Y yo lo que quiero es quedarme solamente 
# con el primer nombre. Cómo hago? Porque es una lista, que elijo la primera posición que es el nombre pero necesito
# a su vez quedarme con la primera posición de ese primer elemento. Bueno, uso la función de split (que significa partir). Veamos: 

print("--------------------------------------------------")

Persona_4 = ["Juan Pablo", "Ramos", 4, "Tel 15564"]
print(Persona_4[0].split( ))
# hasta acá me va a dividir el primer elemento, es decir el nombre, en este caso en dos veces. Dónde lo divide?
# donde reconoce que hay un espacio en blanco. Si a eso le agrego la posición, me quedará solo el primer nombre. 

print(Persona_4[0].split(-2))



