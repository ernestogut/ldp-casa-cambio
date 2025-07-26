from src.domain.ports.metodo_deposito_repository import MetodoDepositoRepository
from src.domain.models.metodo_deposito import MetodoDeposito
from typing import Optional


class MetodoDepositoService:
    def __init__(self, repository: MetodoDepositoRepository):
        self.repository = repository

    def obtener_metodo_deposito_por_id(
        self, metodo_id: int
    ) -> Optional[MetodoDeposito]:
        return self.repository.obtener_metodo_deposito_por_id(metodo_id)
