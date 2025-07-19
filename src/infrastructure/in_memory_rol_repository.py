from src.domain.models.rol import Rol
from src.domain.ports.rol_repository import RolRepository as RolRepositoryPort


class InMemoryRolRepository(RolRepositoryPort):
    def obtener_rol_por_id(self, rol_id: int) -> Rol | None:
        for rol in self.roles:
            if rol.id_rol == rol_id:
                return rol
        return None

    def __init__(self):
        self.roles = [
            Rol(id_rol=1, nombre="Administrador"),
            Rol(id_rol=2, nombre="Usuario"),
        ]

    def obtener_rol(self, rol_input: str) -> tuple[int, str]:
        if rol_input == "1":
            return self.roles[0].id_rol, self.roles[0].nombre
        elif rol_input == "2":
            return self.roles[1].id_rol, self.roles[1].nombre
        else:
            print(
                "Rol no válido. Por favor, elige entre Administrador (1) o Usuario (2)."
            )
            return -1, ""
