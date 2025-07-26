from src.domain.ports.tasa_cambio_repository import TasaCambioRepository
from src.domain.models.tasa_cambio import TasaCambio
from src.domain.models.moneda import Moneda
from typing import List, Optional


class InMemoryTasaCambioRepository(TasaCambioRepository):
    def __init__(self):
        self.tasas = {}
        usd = Moneda("USD", "$", "Dólares")
        clp = Moneda("CLP", "CLP$", "Pesos Chilenos")
        cop = Moneda("COP", "COP$", "Pesos Colombianos")
        bob = Moneda("BOB", "Bs.", "Pesos Bolivianos")
        pen = Moneda("PEN", "S/", "Soles")
        self.agregar_tasa(TasaCambio(pen, usd, 0.27))
        self.agregar_tasa(TasaCambio(pen, clp, 220.0))
        self.agregar_tasa(TasaCambio(pen, cop, 1000.0))
        self.agregar_tasa(TasaCambio(pen, bob, 1.85))
        self.agregar_tasa(TasaCambio(usd, pen, 3.70))
        self.agregar_tasa(TasaCambio(clp, pen, 0.0041))
        self.agregar_tasa(TasaCambio(cop, pen, 0.00098))
        self.agregar_tasa(TasaCambio(bob, pen, 0.54))

    def agregar_tasa(self, tasa: TasaCambio) -> None:
        key = self._make_key(tasa.moneda_origen, tasa.moneda_destino)
        self.tasas[key] = tasa

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

    def _make_key(self, moneda_origen: Moneda, moneda_destino: Moneda) -> str:
        return f"{moneda_origen.codigo}->{moneda_destino.codigo}"
