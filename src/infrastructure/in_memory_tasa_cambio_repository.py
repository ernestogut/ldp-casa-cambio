from src.domain.ports.tasa_cambio_repository import TasaCambioRepository
from src.domain.models.tasa_cambio import TasaCambio
from typing import List, Optional


class InMemoryTasaCambioRepository(TasaCambioRepository):
    def __init__(self):
        self.tasas: dict[str, TasaCambio] = {}
        self.agregar_tasa(TasaCambio("USD", "Dólares", "$", 3.70))
        self.agregar_tasa(TasaCambio("CLP", "Pesos Chilenos", "CLP$", 0.0041))
        self.agregar_tasa(TasaCambio("COP", "Pesos Colombianos", "COP$", 0.00098))
        self.agregar_tasa(TasaCambio("BOB", "Pesos Bolivianos", "Bs.", 0.54))
        self.agregar_tasa(TasaCambio("PEN", "Soles", "S/", 1.0))

    def agregar_tasa(self, tasa: TasaCambio) -> None:
        self.tasas[tasa.codigo] = tasa

    def actualizar_tasa(self, codigo: str, nueva_tasa: float) -> None:
        if codigo in self.tasas:
            self.tasas[codigo].tasa = nueva_tasa

    def eliminar_tasa(self, codigo: str) -> None:
        if codigo in self.tasas:
            del self.tasas[codigo]

    def obtener_tasa(self, codigo: str) -> Optional[TasaCambio]:
        return self.tasas.get(codigo)

    def listar_tasas(self) -> List[TasaCambio]:
        return list(self.tasas.values())
