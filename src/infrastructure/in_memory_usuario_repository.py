from src.domain.models.usuario import Usuario
from src.domain.models.rol import Rol
from src.domain.ports.usuario_repository import (
    UsuarioRepository as UsuarioRepositoryPort,
)


class InMemoryUsuarioRepository(UsuarioRepositoryPort):
    def __init__(self):
        self.usuarios: list[Usuario] = []
        self.usuarios.append(
            Usuario(
                nombre="Sistema",
                dni="12345678",
                cuenta_bancaria="1234567890",
                email="sistema@gmail.com",
                contrasena="root",
                rol=Rol(id_rol=1, nombre="Administrador"),
            )
        )

    def crear_usuario(self, usuario: Usuario) -> None:
        self.usuarios.append(usuario)

    def obtener_usuarios(self) -> list[Usuario]:
        return self.usuarios

    def obtener_usuario_por_email(self, email: str) -> Usuario | None:
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None

    def eliminar_usuario(self, email: str) -> None:
        self.usuarios = [u for u in self.usuarios if u.email != email]

    def iniciar_sesion(self, email: str, contrasena: str) -> Usuario | None:
        return next(
            (
                u
                for u in self.usuarios
                if u.email == email and u.contrasena == contrasena
            ),
            None,
        )
