from src.domain.ports.tasa_cambio_repository import TasaCambioRepository
from src.domain.models.tasa_cambio import TasaCambio
from typing import Optional, List


class TasaCambioService:
    def __init__(self, tasa_repo: TasaCambioRepository):
        self.tasa_repo = tasa_repo

    def agregar_tasa(self, codigo: str, nombre: str, simbolo: str, tasa: float) -> None:
        nueva_tasa = TasaCambio(codigo, nombre, simbolo, tasa)
        self.tasa_repo.agregar_tasa(nueva_tasa)

    def actualizar_tasa(self, codigo: str, nueva_tasa: float) -> None:
        self.tasa_repo.actualizar_tasa(codigo, nueva_tasa)

    def eliminar_tasa(self, codigo: str) -> None:
        self.tasa_repo.eliminar_tasa(codigo)

    def obtener_tasa(self, codigo: str) -> Optional[TasaCambio]:
        return self.tasa_repo.obtener_tasa(codigo)

    def listar_tasas(self) -> List[TasaCambio]:
        return self.tasa_repo.listar_tasas()
