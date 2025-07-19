class TasaCambio:
    def __init__(self, codigo, nombre, simbolo, tasa):
        self.codigo = codigo
        self.nombre = nombre
        self.simbolo = simbolo
        self.tasa = tasa

    def __str__(self):
        return f"{self.nombre} ({self.simbolo}) - Tasa: {self.tasa}"

    def __getitem__(self, key):
        return getattr(self, key, None)
