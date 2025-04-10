def mensaje_motivacional():
    print("Mensaje motivacional")

def lista_nombres ():
    nombres=["Dilii", "Dilana", "Ruth"]    
    for nombre in nombres:
        print(f"->{nombre}")



def menu():
    while True:
        print("1.mensaje motivacional")
        print("2.Lista de nombres")
        print("3.Salir")
        opcion = input("Seleccione la opcion")
        
        if opcion=="1":
            mensaje_motivacional()
        elif opcion =="2": 
            lista_nombres()
        elif opcion== "3":
            print("graciass")
            break    

menu()