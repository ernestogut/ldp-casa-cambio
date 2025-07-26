from .moneda import Moneda


class TasaCambio:
    def __init__(self, moneda_origen: Moneda, moneda_destino: Moneda, tasa: float):
        self.moneda_origen = moneda_origen
        self.moneda_destino = moneda_destino
        self.tasa = tasa

    def __str__(self):
        return f"{self.moneda_origen} -> {self.moneda_destino} | Tasa: {self.tasa}"

    def __getitem__(self, key):
        return getattr(self, key, None)
