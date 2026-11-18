from clases import Client, BankAccount
#

activo = True

while activo:
    print("Bienvenido al sistema bancario")
    print("1. Crear un cliente")
    print("2. Crear una cuenta bancaria para un cliente")
    print("3. Ingresar dinero en la cuenta")
    print("4. Sacar dinero de la cuenta")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "5":
        activo = False
        print("Chao pescao")

    elif opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        pinvalido = False
        while not(pinvalido):
            pin1 = input("Ingrese el PIN del cliente: ")
            pin2 = input("Ingrese el PIN de nuevo para confirmarlo: ")
            if pin1 == pin2:
                pinvalido = True
                pin = pin1
            else:
                print("Los PINs no coinciden. Intente de nuevo.")
        cliente = Client(nombre, apellido, pin)
        print(f"Cliente creado: {cliente}")

    elif opcion == "2":
        numero_cuenta = 0

    
    elif opcion == "4":
        pass

    elif opcion == "3":
        pass
