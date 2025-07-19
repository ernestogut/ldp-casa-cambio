from models.transaccion import Transaccion
import datetime

TASAS_CAMBIO = {
    "USD": {"nombre": "Dólares", "simbolo": "$", "tasa": 3.70},
    "CLP": {"nombre": "Pesos Chilenos", "simbolo": "CLP$", "tasa": 0.0041},
    "COP": {"nombre": "Pesos Colombianos", "simbolo": "COP$", "tasa": 0.00098},
    "BOB": {"nombre": "Pesos Bolivianos", "simbolo": "Bs.", "tasa": 0.54},
    "PEN": {"nombre": "Soles", "simbolo": "S/", "tasa": 1.0}
}

OPCIONES_MONEDA = {
    "1": "USD",
    "2": "CLP",
    "3": "COP",
    "4": "BOB",
    "5": "PEN"
}

def flujo_cambio_divisas(usuario):
    while True:
        print("\n=== Cambio de Divisas ===")
        print("Monedas disponibles:")

        for num, codigo in OPCIONES_MONEDA.items():
            info = TASAS_CAMBIO[codigo]
            print(f"{num}. {info['nombre']} ({info['simbolo']})")

        print("Escribe 'salir' en cualquier momento para volver al menú anterior.\n")

        moneda_origen_input = input("Elige la moneda origen (1-5): ").strip()
        if moneda_origen_input.lower() == "salir":
            break
        if moneda_origen_input not in OPCIONES_MONEDA:
            print("Opción de moneda origen no válida.\n")
            continue

        moneda_destino_input = input("Elige la moneda destino (1-5): ").strip()
        if moneda_destino_input.lower() == "salir":
            break
        if moneda_destino_input not in OPCIONES_MONEDA:
            print("Opción de moneda destino no válida.\n")
            continue

        moneda_origen = OPCIONES_MONEDA[moneda_origen_input]
        moneda_destino = OPCIONES_MONEDA[moneda_destino_input]

        if moneda_origen == moneda_destino:
            print("No puedes cambiar a la misma moneda.\n")
            continue

        try:
            simbolo_origen = TASAS_CAMBIO[moneda_origen]['simbolo']
            simbolo_destino = TASAS_CAMBIO[moneda_destino]['simbolo']
            nombre_origen = TASAS_CAMBIO[moneda_origen]['nombre']
            nombre_destino = TASAS_CAMBIO[moneda_destino]['nombre']

            monto_origen = float(input(f"Ingrese el monto en {nombre_origen} ({simbolo_origen}): "))

            tasa_origen = TASAS_CAMBIO[moneda_origen]['tasa']
            tasa_destino = TASAS_CAMBIO[moneda_destino]['tasa']

            monto_destino = monto_origen * (tasa_origen / tasa_destino)

            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            nueva_transaccion = Transaccion(
                monto_origen,
                monto_destino,
                fecha,
                simbolo_origen,
                simbolo_destino,
                nombre_origen,
                nombre_destino
            )
            usuario.agregar_transaccion(nueva_transaccion)

            print(f"\nCambio exitoso: {simbolo_origen}{monto_origen:.2f} -> {simbolo_destino}{monto_destino:.2f}")
            print(f"({nombre_origen} -> {nombre_destino})\n")
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
