from src.domain.models.metodo_deposito import MetodoDeposito
from src.domain.ports.metodo_deposito_repository import MetodoDepositoRepository


class InMemoryMetodoDepositoRepository(MetodoDepositoRepository):

    def __init__(self):
        self.metodos = [
            MetodoDeposito(
                id=1,
                nombre="Transferencia bancaria",
                descripcion="Depósito a través de transferencia bancaria",
            ),
            MetodoDeposito(id=2, nombre="Yape", descripcion="Depósito utilizando Yape"),
            MetodoDeposito(id=3, nombre="Plin", descripcion="Depósito utilizando Plin"),
        ]

    def obtener_metodo_deposito_por_id(self, metodo_id: int) -> MetodoDeposito | None:
        for metodo in self.metodos:
            if metodo.id == metodo_id:
                return metodo
        return None

    def obtener_todos_metodos_deposito(self) -> list[MetodoDeposito]:
        return self.metodos
