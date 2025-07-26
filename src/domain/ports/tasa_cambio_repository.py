from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.models.tasa_cambio import TasaCambio


class TasaCambioRepository(ABC):
    @abstractmethod
    def agregar_tasa(self, tasa: TasaCambio) -> None:
        pass

    @abstractmethod
    def actualizar_tasa(self, codigo: str, nueva_tasa: float) -> None:
        pass

    @abstractmethod
    def eliminar_tasa(self, codigo: str) -> None:
        pass

    @abstractmethod
    def obtener_tasa(self, codigo: str) -> Optional[TasaCambio]:
        pass

    @abstractmethod
    def listar_tasas(self) -> List[TasaCambio]:
        pass
