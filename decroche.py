#Quejas o problemas
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
print(quejas())

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
    return tuplas
print(horarios())