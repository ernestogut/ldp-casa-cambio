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
            print("Tasas disponibles:")
            tasas = self.tasa_cambio_service.listar_tasas()
            opciones = {
                str(i + 1): f"{t.moneda_origen.codigo}->{t.moneda_destino.codigo}"
                for i, t in enumerate(tasas)
            }
            for num, key in opciones.items():
                t = self.tasa_cambio_service.obtener_tasa(key)
                if not t:
                    continue
                print(
                    f"{num}. {t.moneda_origen.nombre} ({t.moneda_origen.simbolo}) -> {t.moneda_destino.nombre} ({t.moneda_destino.simbolo}) | Tasa: {t.tasa}"
                )
            print(
                "Escribe 'salir' en cualquier momento para volver al menú anterior.\n"
            )
            tasa_key_input = input(f"Elige la tasa (1-{len(opciones)}): ").strip()
            if tasa_key_input.lower() == "salir":
                break
            if tasa_key_input not in opciones:
                print("Opción de tasa no válida.\n")
                continue
            key = opciones[tasa_key_input]
            tasa_obj = self.tasa_cambio_service.obtener_tasa(key)
            if not tasa_obj:
                print("Tasa no encontrada.\n")
                continue
            try:
                monto_origen = float(
                    input(
                        f"Ingrese el monto en {tasa_obj.moneda_origen.nombre} ({tasa_obj.moneda_origen.simbolo}): "
                    )
                )
                monto_destino = monto_origen * tasa_obj.tasa
                fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                nueva_transaccion = Transaccion(
                    monto_origen,
                    monto_destino,
                    fecha,
                    tasa_obj.moneda_origen,
                    tasa_obj.moneda_destino,
                )
                self.transaccion_repo.agregar_transaccion(usuario.id, nueva_transaccion)
                print(
                    f"\nCambio exitoso: {tasa_obj.moneda_origen.simbolo}{monto_origen:.2f} -> {tasa_obj.moneda_destino.simbolo}{monto_destino:.2f}. El monto sera depositado en tu método de depósito favorito ({usuario.metodo_deposito_fav.nombre})."
                )
                print(
                    f"({tasa_obj.moneda_origen.nombre} -> {tasa_obj.moneda_destino.nombre})\n"
                )
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
