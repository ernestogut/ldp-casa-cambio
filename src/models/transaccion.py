class Transaccion:
    def __init__(self, monto_dolares, monto_soles, tasa_cambio, fecha):
        self.monto_dolares = monto_dolares
        self.monto_soles = monto_soles
        self.tasa_cambio = tasa_cambio
        self.fecha = fecha

    def __str__(self):
        return (
            f"{self.fecha} | ${self.monto_dolares:.2f} -> S/ {self.monto_soles:.2f} "
            f"(Tasa: {self.tasa_cambio})"
        )
