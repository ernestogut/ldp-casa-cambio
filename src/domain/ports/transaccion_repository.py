from abc import ABC, abstractmethod
from typing import List
from src.domain.models.transaccion import Transaccion


class TransaccionRepository(ABC):
    @abstractmethod
    def agregar_transaccion(self, usuario_id: int, transaccion: Transaccion) -> None:
        pass

    @abstractmethod
    def obtener_transacciones(self, usuario_id: int) -> List[Transaccion]:
        pass
