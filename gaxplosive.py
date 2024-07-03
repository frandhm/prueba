from funciones import *

while True:
    print("Menu Gaxplosive")

    print("""
1. Registrar Pedido
2. Lista Todos los pedidos
3. Buscar pedido por RUT
4. Imprimir hoja de ruta
5. Salir
""")
    opc = int(input("Escoga una opción: "))

    if opc == 1:
        registrar_pedido()
    elif opc == 2:
        pass
    elif opc == 3:
        pass
    elif opc == 4:
        pass
    elif opc == 5:
        salir()
    else:
        print("Error! Escoga una opción valida!")