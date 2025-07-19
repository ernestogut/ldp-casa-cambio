class Transaccion:
    def __init__(self, monto_origen, monto_destino, fecha, moneda_origen, moneda_destino, nombre_origen, nombre_destino):
        self.monto_origen = monto_origen
        self.monto_destino = monto_destino
        self.fecha = fecha
        self.moneda_origen = moneda_origen  # Símbolo
        self.moneda_destino = moneda_destino  # Símbolo
        self.nombre_origen = nombre_origen    # Nombre de la moneda
        self.nombre_destino = nombre_destino  # Nombre de la moneda

    def __str__(self):
        return (
            f"{self.fecha} | {self.moneda_origen}{self.monto_origen:.2f} -> "
            f"{self.moneda_destino}{self.monto_destino:.2f} "
            f"({self.nombre_origen} -> {self.nombre_destino})"
        )
