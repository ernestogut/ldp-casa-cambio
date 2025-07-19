from models.transaccion import Transaccion
from models.moneda import Moneda
from models.tasa_cambio import TasaCambio
import datetime

TASAS_CAMBIO = {
    "USD": TasaCambio("USD", "Dólares", "$", 3.70),
    "CLP": TasaCambio("CLP", "Pesos Chilenos", "CLP$", 0.0041),
    "COP": TasaCambio("COP", "Pesos Colombianos", "COP$", 0.00098),
    "BOB": TasaCambio("BOB", "Pesos Bolivianos", "Bs.", 0.54),
    "PEN": TasaCambio("PEN", "Soles", "S/", 1.0),
}

OPCIONES_MONEDA = {"1": "USD", "2": "CLP", "3": "COP", "4": "BOB", "5": "PEN"}

def actualizar_tasas():
    print("\n=== Actualizar Tasas de Cambio ===")
    for codigo, tasa in TASAS_CAMBIO.items():
        print(f"{codigo}: {tasa.nombre} ({tasa.simbolo}) - Valor actual: {tasa.tasa} PEN")
        try:
            nuevo_valor = input(f"Ingrese nuevo valor para {codigo} o presione Enter para mantener {tasa.tasa}: ")
            if nuevo_valor.strip():
                tasa.tasa = float(nuevo_valor)
                print(f"✔ Tasa actualizada para {codigo}.")
            else:
                print(f"✔ Tasa de {codigo} no modificada.")
        except ValueError:
            print("⚠ Valor inválido. No se actualizó esta tasa.")



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

        moneda_origen_codigo = OPCIONES_MONEDA[moneda_origen_input]
        moneda_destino_codigo = OPCIONES_MONEDA[moneda_destino_input]

        if moneda_origen_codigo == moneda_destino_codigo:
            print("No puedes cambiar a la misma moneda.\n")
            continue

        try:
            info_origen = TASAS_CAMBIO[moneda_origen_codigo]
            info_destino = TASAS_CAMBIO[moneda_destino_codigo]

            monto_origen = float(
                input(
                    f"Ingrese el monto en {info_origen['nombre']} ({info_origen['simbolo']}): "
                )
            )

            tasa_origen = info_origen["tasa"]
            tasa_destino = info_destino["tasa"]

            if tasa_origen is None or tasa_destino is None:
                print(
                    "Error: La tasa de cambio no está disponible para una de las monedas seleccionadas.\n"
                )
                continue

            monto_destino = monto_origen * (tasa_origen / tasa_destino)

            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            moneda_origen = Moneda(info_origen["simbolo"], info_origen["nombre"])
            moneda_destino = Moneda(info_destino["simbolo"], info_destino["nombre"])

            nueva_transaccion = Transaccion(
                monto_origen, monto_destino, fecha, moneda_origen, moneda_destino
            )
            usuario.agregar_transaccion(nueva_transaccion)

            print(
                f"\nCambio exitoso: {info_origen['simbolo']}{monto_origen:.2f} -> {info_destino['simbolo']}{monto_destino:.2f}"
            )
            print(f"({info_origen['nombre']} -> {info_destino['nombre']})\n")
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
