class MetodoDeposito:
    def __init__(self, id: int, nombre: str, descripcion: str):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.id} - {self.nombre} | {self.descripcion}"

    def __getitem__(self, key):
        return getattr(self, key, None)
