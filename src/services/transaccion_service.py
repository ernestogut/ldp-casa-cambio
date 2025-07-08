from models.transaccion import Transaccion
import datetime


def flujo_cambio_divisas(usuario):
    print("\n=== Cambio de Dólares a Soles ===")
    try:
        monto_dolares = float(input("Ingresa el monto en dólares: "))
        tasa_cambio = 3.70
        monto_soles = monto_dolares * tasa_cambio
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        nueva_transaccion = Transaccion(monto_dolares, monto_soles, tasa_cambio, fecha)
        usuario.agregar_transaccion(nueva_transaccion)

        print(f"Cambio exitoso: ${monto_dolares:.2f} -> S/ {monto_soles:.2f}\n")
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
