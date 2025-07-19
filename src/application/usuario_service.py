from src.domain.models.usuario import Usuario
from src.domain.models.rol import Rol
from src.domain.ports.usuario_repository import UsuarioRepository
from src.domain.ports.rol_repository import RolRepository
from src.utils.validations import (
    validar_email,
    validar_dni,
    validar_cuenta_bancaria,
    email_existe,
)
from getpass import getpass


class UsuarioService:
    def __init__(self, usuario_repo: UsuarioRepository, rol_repo: RolRepository):
        self.usuario_repo = usuario_repo
        self.rol_repo = rol_repo

    def registrar_usuario(self):
        print("\n=== Registro de Usuario ===")
        nombre = input("Nombre: ")

        while True:
            email = input("Email: ")
            if not validar_email(email):
                print("Email inválido. Debe contener '@' y un dominio.")
                continue
            if email_existe(email, self.usuario_repo.obtener_usuarios()):
                print("Este email ya está registrado. Usa otro.")
                continue
            break

        while True:
            dni = input("DNI: ")
            if not validar_dni(dni):
                print("DNI inválido. Debe tener 8 dígitos.")
                continue
            break

        while True:
            cuenta = input("Cuenta bancaria: ")
            if not validar_cuenta_bancaria(cuenta):
                print("Cuenta bancaria inválida. Debe tener al menos 10 caracteres.")
                continue
            break

        contrasena = getpass("Contraseña: ")
        rol_id_input = input("Rol (1: Administrador, 2: Usuario): ").strip()
        try:
            rol_id = int(rol_id_input)
        except ValueError:
            print("ID de rol inválido. Se asigna rol Usuario por defecto.")
            rol_id = 2
        rol = self.rol_repo.obtener_rol_por_id(rol_id)
        if not rol:
            print("Rol no encontrado. Se asigna rol Usuario por defecto.")
            rol = self.rol_repo.obtener_rol_por_id(2)
            if not rol:
                rol = Rol(id_rol=2, nombre="Usuario")

        usuario = Usuario(
            nombre=nombre,
            email=email,
            dni=dni,
            cuenta_bancaria=cuenta,
            contrasena=contrasena,
            rol=rol,
        )
        self.usuario_repo.crear_usuario(usuario)
        print("Usuario registrado con éxito.\n")

    def mostrar_usuarios(self):
        print("\n=== Usuarios Registrados ===")
        usuarios = self.usuario_repo.obtener_usuarios()
        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            for i, usuario in enumerate(usuarios, start=1):
                print(f"{i}. {usuario}")

    def iniciar_sesion(self):
        print("\n=== Iniciar sesión ===")
        email = input("Email: ")
        contrasena = getpass("Contraseña: ")
        usuario = self.usuario_repo.iniciar_sesion(email, contrasena)
        if usuario:
            print(f"Bienvenido, {usuario.nombre}!\n")
            return usuario
        print("Email o contraseña incorrectos.\n")
        return None
