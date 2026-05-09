ingreso = True
while ingreso:
    print("--Menu--")
    print("1. Pago Tarjeta de Crédito")
    print("2. Simulación de compras")
    print("3. Salir")
    op = int(input("Ingrese su opción: "))

    if op == 1:
        print("Pagando...")
    elif op == 2: 
        print("Comprando...")
    elif op == 3:
        print("Saliendo...")
        #break
        ingreso = False
    else:
        print("Opción no válida!")
