from abc import ABC, abstractmethod
from typing import Optional
from src.domain.models.rol import Rol


class RolRepository(ABC):

    @abstractmethod
    def obtener_rol_por_id(self, rol_id: int) -> Optional["Rol"]:
        """Obtiene un rol por su ID."""
        pass
