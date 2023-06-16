#Quejas o problemas
salir = False
opcion = 0
def quejas():
    print("Deja aquí tu mensaje y tu respuesta vendrá de uno de nuestros asesores")
    lista=[]
    while lista != 4:
        Nombre=input("Ingresa tu nombre: ")
        lista.append(Nombre)
        Correo=input("Tu correo: ")
        lista.append(Correo)
        Numero_pedido=str(input("Ingresa el numero de tu pedido: "))
        lista.append(Numero_pedido)
        Mensaje=input("Escribe de manera breve el problema que presentas con tu producto: ")
        lista.append(Mensaje)
        if len (Mensaje)>40:
              print("Tu mensaje debe ser más corto")
        lista.sort()
        print("Datos ingresados: ", len(lista))
        print("Seras contactado de inmediato con uno de nuestros asesores")
        print(lista)
        salir=False
    return

# Horarios de atencion
def horarios():
    tupla=("Lunes: 7am a 7pm")
    print(tupla)
    tupla_2=("Martes: 7am a 7pm")
    print(tupla_2)
    tupla_3=("Miercoles: 7am a 7pm")
    print(tupla_3)
    tupla_4=("Jueves: 7am a 7pm")
    print(tupla_4)
    tupla_5=("Viernes: 7am a 7pm")
    print(tupla_5)
    tupla_6=("Sábado:7am a 7pm")
    print(tupla_6)
    tuplas=("Estos son nuestros horarios de atención")
    salir=False
    return tuplas
#menu

 
while not salir:
 
    print ("1. Realizar una queja o reclamo")
    print ("2. Visualizar los horarios")
    print ("3. Realizar una compra")
    print ("4. Acerca de nosotros")
     
    print ("Elige una opcion")

 
    if opcion == 1:
        print (quejas())
    elif opcion == 2:
        print (horarios())
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")