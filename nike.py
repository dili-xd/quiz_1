datos={
    "producto":"suter",
    "talla":"xs",
    "color":"negro"
}

def mostrar():
    for producto,detalle in datos.items():
        print(f"Datos diccionario {producto}-{detalle}")

def actualizar ():
    clave_cambio = input ("Cambiar prodcto: \n")
    if clave_cambio in datos:
        nuevo_valor =input("Cambiar nuevo valor: \n")
        datos[clave_cambio]=nuevo_valor
    else:
        print("Clave inexistente ")
    print(datos)

def eliminar ():
    clave_eliminar= input ("Ingrese la clave a eliminar: \n")
    if clave_eliminar in datos:
        del datos [clave_eliminar]
    else:
        print ("Clave inexistente")
    print(datos)    

def menu():
    while True:
        print("1-Ver diccionario")
        print("2-Actualizar")
        print("3-Eliminar")
        print("4-Salir")
        opcion =input("seleccione una opcion: \n")

        if opcion=="1":
            mostrar()
        elif opcion=="2":
            actualizar()
        elif opcion=="3":
            eliminar()
        elif opcion=="4":
            print("salir")
            break
            
            
menu()         


