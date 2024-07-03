import os, csv

cilindro_5 = 12500
cilindro_15 = 25500
pedidos = []

comunas = ["Puente Alto", "La Florida", "La Cisterna"]
def registrar_pedido():
    cil5 = 0
    cil15 = 0
    rut = input("Ingrese su RUT: ")
    name = input("Indique su nombre: ")
    direccion = input("Ingrese su dirección: ")
    print("Comunas que atendemos (1.Puente alto, 2.La florida, 3.La cisterna)")
    comuna = int(input("Ingrese el número de su comuna"))
    while True:
        opcion = int(input("1.Cilindro de 5kg\n2.Cilindro de 15 kg\n3.Continuar\nElija el producto que desea:"))
        if opcion == 1:
            cil5 += 1
        elif opcion == 2:
            cil15 += 1
        elif opcion == 3:
            break
        else:
            print("Error! Ingrese una opción valida")
    total = cil5 + cil15

    pedido = [rut, name, direccion, comunas[comuna-1], f"Cilindro de 5 ={cil5}", f"cilindro de 15 ={cil15}",total]

    pedidos.append(pedido)        
        
def salir():
    print("Chao, hasta la proxima")
    exit()

