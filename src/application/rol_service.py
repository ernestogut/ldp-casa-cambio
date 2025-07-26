from src.domain.ports.rol_repository import RolRepository
from src.domain.models.rol import Rol
from typing import Optional


class RolService:
    def __init__(self, repository: RolRepository):
        self.repository = repository

    def obtener_rol_por_id(self, rol_id: int) -> Optional[Rol]:
        return self.repository.obtener_rol_por_id(rol_id)
