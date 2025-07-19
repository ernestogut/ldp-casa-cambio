from src.domain.ports.transaccion_repository import TransaccionRepository
from .tasa_cambio_service import TasaCambioService
from src.domain.models.transaccion import Transaccion
from src.domain.models.moneda import Moneda
from src.domain.models.usuario import Usuario
import datetime


OPCIONES_MONEDA = {"1": "USD", "2": "CLP", "3": "COP", "4": "BOB", "5": "PEN"}


class TransaccionService:
    def __init__(
        self,
        transaccion_repo: TransaccionRepository,
        tasa_cambio_service: TasaCambioService,
    ):
        self.transaccion_repo = transaccion_repo
        self.tasa_cambio_service = tasa_cambio_service

    def flujo_cambio_divisas(self, usuario: Usuario):
        while True:
            print("\n=== Cambio de Divisas ===")
            print("Monedas disponibles:")
            tasas = self.tasa_cambio_service.listar_tasas()
            opciones = {str(i + 1): t.codigo for i, t in enumerate(tasas)}
            for num, codigo in opciones.items():
                info = self.tasa_cambio_service.obtener_tasa(codigo)
                if not info:
                    continue
                print(f"{num}. {info.nombre} ({info.simbolo})")
            print(
                "Escribe 'salir' en cualquier momento para volver al menú anterior.\n"
            )
            moneda_origen_input = input(
                f"Elige la moneda origen (1-{len(opciones)}): "
            ).strip()
            if moneda_origen_input.lower() == "salir":
                break
            if moneda_origen_input not in opciones:
                print("Opción de moneda origen no válida.\n")
                continue
            moneda_destino_input = input(
                f"Elige la moneda destino (1-{len(opciones)}): "
            ).strip()
            if moneda_destino_input.lower() == "salir":
                break
            if moneda_destino_input not in opciones:
                print("Opción de moneda destino no válida.\n")
                continue
            moneda_origen_codigo = opciones[moneda_origen_input]
            moneda_destino_codigo = opciones[moneda_destino_input]
            if moneda_origen_codigo == moneda_destino_codigo:
                print("No puedes cambiar a la misma moneda.\n")
                continue
            try:
                info_origen = self.tasa_cambio_service.obtener_tasa(
                    moneda_origen_codigo
                )
                info_destino = self.tasa_cambio_service.obtener_tasa(
                    moneda_destino_codigo
                )
                if not info_origen or not info_destino:
                    print(
                        "Error: La tasa de cambio no está disponible para una de las monedas seleccionadas.\n"
                    )
                    continue
                monto_origen = float(
                    input(
                        f"Ingrese el monto en {info_origen.nombre} ({info_origen.simbolo}): "
                    )
                )
                tasa_origen = info_origen.tasa
                tasa_destino = info_destino.tasa
                if tasa_origen is None or tasa_destino is None:
                    print(
                        "Error: La tasa de cambio no está disponible para una de las monedas seleccionadas.\n"
                    )
                    continue
                monto_destino = monto_origen * (tasa_origen / tasa_destino)
                fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                moneda_origen = Moneda(info_origen.simbolo, info_origen.nombre)
                moneda_destino = Moneda(info_destino.simbolo, info_destino.nombre)
                nueva_transaccion = Transaccion(
                    monto_origen, monto_destino, fecha, moneda_origen, moneda_destino
                )
                self.transaccion_repo.agregar_transaccion(usuario.id, nueva_transaccion)
                print(
                    f"\nCambio exitoso: {info_origen.simbolo}{monto_origen:.2f} -> {info_destino.simbolo}{monto_destino:.2f}"
                )
                print(f"({info_origen.nombre} -> {info_destino.nombre})\n")
            except ValueError:
                print("Por favor ingresa un número válido.\n")

    def ver_transacciones(self, usuario):
        print("\n=== Mis Transacciones ===")
        transacciones = self.transaccion_repo.obtener_transacciones(usuario.id)
        if not transacciones:
            print("No tienes transacciones registradas.")
        else:
            for i, tx in enumerate(transacciones, start=1):
                print(f"{i}. {tx}")
        print()
