from abc import ABC, abstractmethod
from typing import Optional
from src.domain.models.metodo_deposito import MetodoDeposito


class MetodoDepositoRepository(ABC):

    @abstractmethod
    def obtener_metodo_deposito_por_id(
        self, metodo_id: int
    ) -> Optional["MetodoDeposito"]:
        """Obtiene un método de depósito por su ID."""
        pass

    @abstractmethod
    def obtener_todos_metodos_deposito(self) -> list[MetodoDeposito]:
        """Obtiene todos los métodos de depósito disponibles."""
        pass
