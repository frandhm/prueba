import os, time

cilindro_5 = 12500
cilindro_15 = 25500
pedidos = []
comunas = ["Puente Alto", "La Florida", "La Cisterna"]

def registrar_pedido():
    limpiar()
    cil5 = 0
    cil15 = 0
    rut = validarRut()
    name = validarNombre()
    direccion = validarDireccion()
    comuna = validarComuna()
    validarCompraCilindro()
    total = (cilindro_5*cil5) + (cilindro_15*cil15)
    pedido = [rut, name, direccion, comunas[comuna-1], cil5, cil15,total]
    pedidos.append(pedido)
    print("Pedido realizado con exito!")
    espera(2)   
        
def lista_pedidos():
    limpiar()
    if not pedidos:
        print("No existen pedidos, por favor ingrese alguno")
        espera(2)
    else:
        limpiar()
        print("Lista de pedidos")
        for i in pedidos:
            print(pedidos[i])

def buscar_pedidos():
    limpiar()
    if not pedidos:
        print("No existen pedidos, por favor ingrese alguno")
    else:
        rut = int(input("Ingrese su rut: "))
        for i in pedidos:
            if rut in(pedidos):
                print(pedidos[i])
            else:
                print("No existe un pedido con ese rut!")

def imprimirHoja():
    limpiar()
    import csv
    if not pedidos:
        print("Error no hay pedidos para exportar")
    else:
        name = input("Ingrese el nombre del archivo que desea exportar: ")+".csv"
        with open(name,"w",newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(pedidos)
        print("Archivo exportado con exito!")
        espera(2)






def salir():
    limpiar()
    print("Chao, hasta la proxima")
    exit()

def limpiar():
    os.system("cls")

def validarRut():
    while True:
        try:
            rut = int(input("Ingrese su RUT (sin puntos ni guion): "))
            if len(str(rut)) == 9:
                print("Rut valido")
                espera(2)
                break
            else:
                print("Error debe ingresar un rut valido")
        except:
            print("Error! Ingrese solo números")

def validarNombre():
    limpiar()
    while True:
        name = input("Indique su nombre: ")
        if len(name) > 2 and name.isalpha():
            print("nombre guardado con exito")
            espera(2)
            break
        else:
            print("Error nombre no valido")

def validarDireccion():
    limpiar()
    while True:
        direccion = input("Ingrese su dirección: ")
        if len(direccion) >= 3:
            print("Dirección guardada con exito")
            espera(2)
            break
        else:
            print("Error! dirección no valida")

def validarComuna():
    limpiar()
    print("Comunas que atendemos (1.Puente alto, 2.La florida, 3.La cisterna)")
    while True:
        try:
            comuna = int(input("Ingrese el número de su comuna"))
            if comuna >= 1 and comuna <= 3:
                print("Comuna guardada con exito")
                espera(2)
                break
        except:
            print("Error! opción no valida")
    
def validarCompraCilindro():
    limpiar()
    while True:
        try:
            opcion = int(input("1.Cilindro de 5kg\n2.Cilindro de 15 kg\n3.Continuar\nElija el producto que desea:"))
            if opcion >= 1 and opcion <= 3:
                if opcion == 1:
                    cil5 = int(input("¿Cuantos desea?: "))
                    continue
                elif opcion == 2:
                    cil15 = int(input("¿Cuantos desea?: "))
                    continue
                elif opcion == 3:
                    espera(2)
                    return cil5, cil15
                else:
                    print("Error! Ingrese una opción valida")
                        
            else:
                print("Error! Ingrese una opción valida")
        except:
            print("Error! opción no valida!")

def espera(a):
    time.sleep(a)