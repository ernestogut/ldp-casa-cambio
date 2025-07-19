from src.domain.ports.transaccion_repository import TransaccionRepository
from src.domain.models.transaccion import Transaccion
from typing import List, Dict


class InMemoryTransaccionRepository(TransaccionRepository):
    def __init__(self):
        self.transacciones: Dict[int, List[Transaccion]] = {}

    def agregar_transaccion(self, usuario_id: int, transaccion: Transaccion) -> None:
        if usuario_id not in self.transacciones:
            self.transacciones[usuario_id] = []
        self.transacciones[usuario_id].append(transaccion)

    def obtener_transacciones(self, usuario_id: int) -> List[Transaccion]:
        return self.transacciones.get(usuario_id, [])
