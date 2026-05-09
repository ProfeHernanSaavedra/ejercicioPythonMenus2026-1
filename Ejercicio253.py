ingreso = True
saldo = 100000
while ingreso:
    print("--Menu--")
    print("1. Pago Tarjeta de Crédito")
    print("2. Simulación de compras")
    print("3. Salir")
    op = int(input("Ingrese su opción: "))

    if op == 1:
        print("Pagando...")
        montoPagar = int(input("Ingrese monto a pagar: "))
        if montoPagar >= 0 :
            if montoPagar <= saldo :
                saldo = saldo - montoPagar
                print("El saldo de la tarjeta es: $",saldo)
    elif op == 2: 
        print("Comprando...")
    elif op == 3:
        print("Saliendo...")
        #break
        ingreso = False
    else:
        print("Opción no válida!")
