from models.transaccion import Transaccion
import datetime

TASAS_CAMBIO = {
    "1": ("Dólares", 3.70),
    "2": ("Euros", 4.10),
    "3": ("Libras Esterlinas", 4.80),
    "4": ("Yenes", 0.025)
}

def flujo_cambio_divisas(usuario):
    while True:
        print("\n=== Cambio de Divisas ===")
        print("1. Cambiar a Soles")
        print("2. Cambiar de Soles a otra divisa")
        print("3. Volver al menú anterior")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            cambiar_a_soles(usuario)
        elif opcion == "2":
            cambiar_de_soles(usuario)
        elif opcion == "3":
            break
        else:
            print("Opción no válida.\n")

def cambiar_a_soles(usuario):
    print("\n--- Cambiar a Soles ---")
    print("1. Dólares")
    print("2. Euros")
    print("3. Libras Esterlinas")
    print("4. Yenes")
    
    opcion = input("Elige la divisa: ")

    if opcion not in TASAS_CAMBIO:
        print("Opción no válida.\n")
        return

    divisa, tasa_cambio = TASAS_CAMBIO[opcion]
    print(f"Seleccionaste: {divisa} (Tasa: {tasa_cambio})")

    try:
        monto_origen = float(input(f"Ingresa el monto en {divisa}: "))
        monto_soles = monto_origen * tasa_cambio
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        nueva_transaccion = Transaccion(
            monto_origen, monto_soles, tasa_cambio, fecha
        )
        usuario.agregar_transaccion(nueva_transaccion)

        print(f"Cambio exitoso: {monto_origen:.2f} {divisa} -> S/ {monto_soles:.2f}\n")
    except ValueError:
        print("Por favor ingresa un número válido.\n")

def cambiar_de_soles(usuario):
    print("\n--- Cambiar de Soles a otra divisa ---")
    print("1. Dólares")
    print("2. Euros")
    print("3. Libras Esterlinas")
    print("4. Yenes")
    
    opcion = input("Elige la divisa: ")

    if opcion not in TASAS_CAMBIO:
        print("Opción no válida.\n")
        return

    divisa, tasa_cambio = TASAS_CAMBIO[opcion]
    print(f"Seleccionaste: {divisa} (Tasa: {tasa_cambio})")

    try:
        monto_soles = float(input("Ingresa el monto en Soles: "))
        monto_origen = monto_soles / tasa_cambio
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        nueva_transaccion = Transaccion(
            monto_soles, monto_origen, tasa_cambio, fecha
        )
        usuario.agregar_transaccion(nueva_transaccion)

        print(f"Cambio exitoso: S/ {monto_soles:.2f} -> {monto_origen:.2f} {divisa}\n")
    except ValueError:
        print("Por favor ingresa un número válido.\n")

def ver_transacciones(usuario):
    print("\n=== Mis Transacciones ===")
    if not usuario.transacciones:
        print("No tienes transacciones registradas.")
    else:
        for i, tx in enumerate(usuario.transacciones, start=1):
            print(f"{i}. {tx}")
    print()
