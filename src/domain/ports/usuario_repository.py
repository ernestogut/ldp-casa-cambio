from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.models.usuario import Usuario


class UsuarioRepository(ABC):
    @abstractmethod
    def crear_usuario(self, usuario: Usuario) -> None:
        """Crea un nuevo usuario en el repositorio."""
        pass

    @abstractmethod
    def obtener_usuarios(self) -> List[Usuario]:
        """Obtiene todos los usuarios del repositorio."""
        pass

    @abstractmethod
    def iniciar_sesion(self, email: str, contrasena: str) -> Optional[Usuario]:
        """Inicia sesión con el email y la contraseña proporcionados."""
        pass
