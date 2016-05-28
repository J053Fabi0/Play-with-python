#Esta es la primera aplicacion .py que hice en un archivo que no halla sido uno de
#codeCademy

print("")

que_quieres = "" #esta variable almacena lo que digas
pedir_que_escriba = "Dime lo que sea y yo lo dire tambien" #esta variable almacena como pedir que escribas algo, para que no diga lo mismo siempre
while que_quieres == "": #si no escribe nada se repetira hasta que "que_quieres" cambie de valor
	print(pedir_que_escriba) #se imprimen las instrucciones
	que_quieres = raw_input() #se da la oportunidad de que escriba algo
	if que_quieres == "": #si no escribe nada
		pedir_que_escriba = "Escribe algo por favor, no solo des enter:" #las instrucciones cambian


print("")
print ("HEY!! Lo que dijiste fue: " + que_quieres) #se muestra lo que dijiste
print("")
print("")
print("") #espacios o saltos de linea


print("Quieres ver algo aun MAS GENIAL!?")
print("Di si o no, cualquier otra respuesta sera tomada como no")
nombre = ""
si_quiere_mas = ""
pedir_nombre = "Ok. Escribe tu nombre:"
si_quiere_mas = raw_input()

if si_quiere_mas.upper() == "SI":
	while nombre == "":
		print(pedir_nombre)
		nombre = raw_input()
		nombre = " " + nombre + " "
		print (nombre * 400)
		print("")
		print("Esto no te lo esperabas, cierto? jaja")
		print("")
		print("Bueno, eso es todo, gracias por usarme. Adios")
		print("")
else:
	print("Okay, que tengas un buen dia :)")

"""
print("")
print("")
print("Ignora esto de abajo") #en la terminal se muestra "Exit status: 0" y "logout" por eso pido que se ignore
print("")
print(" ||")
print(" ||")
print(" ||")
print("\  /")
print(" \/")
"""