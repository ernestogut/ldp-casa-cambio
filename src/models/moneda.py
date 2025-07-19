class Moneda:
    def __init__(self, simbolo, nombre):
        self.simbolo = simbolo
        self.nombre = nombre

    def __str__(self):
        return f"{self.simbolo} ({self.nombre})"
