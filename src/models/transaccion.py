from .moneda import Moneda
from utils.validations import validar_monto_origen_destino


class Transaccion:
    def __init__(
        self,
        monto_origen: float,
        monto_destino: float,
        fecha: str,
        moneda_origen: Moneda,
        moneda_destino: Moneda,
    ):
        if not validar_monto_origen_destino(monto_origen, monto_destino):
            raise ValueError("El monto no puede ser negativo.")
        self.monto_origen = monto_origen
        self.monto_destino = monto_destino
        self.fecha = fecha
        self.moneda_origen = moneda_origen
        self.moneda_destino = moneda_destino

    def __str__(self) -> str:
        return (
            f"{self.fecha} | "
            f"{self.moneda_origen.simbolo}{self.monto_origen:.2f} -> "
            f"{self.moneda_destino.simbolo}{self.monto_destino:.2f} "
            f"({self.moneda_origen.nombre} -> {self.moneda_destino.nombre})"
        )
