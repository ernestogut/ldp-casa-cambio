from src.domain.models.usuario import Usuario
from src.domain.models.rol import Rol
from src.domain.ports.usuario_repository import UsuarioRepository
from src.domain.ports.rol_repository import RolRepository
from src.domain.ports.metodo_deposito_repository import MetodoDepositoRepository
from src.utils.validations import (
    validar_email,
    validar_dni,
    validar_cuenta_bancaria,
    email_existe,
    validar_telefono,
)
from getpass import getpass


class UsuarioService:
    def __init__(
        self,
        usuario_repo: UsuarioRepository,
        rol_repo: RolRepository,
        metodo_deposito_repo: MetodoDepositoRepository,
    ):
        self.usuario_repo = usuario_repo
        self.rol_repo = rol_repo
        self.metodo_deposito_repo = metodo_deposito_repo

    def registrar_usuario(self, usuario_actual=None):
        print("\n=== Registro de Usuario ===")

        def solicitar_input(mensaje, validador=None, error_msg=None, extra_check=None):
            while True:
                valor = input(mensaje)
                if validador and not validador(valor):
                    if error_msg:
                        print(error_msg)
                    continue
                if extra_check and not extra_check(valor):
                    continue
                return valor

        nombre = input("Nombre: ")
        email = solicitar_input(
            "Email: ",
            validador=validar_email,
            error_msg="Email inválido. Debe contener '@' y un dominio.",
            extra_check=lambda e: not email_existe(
                e, self.usuario_repo.obtener_usuarios()
            )
            or (print("Este email ya está registrado. Usa otro."), False)[1],
        )
        dni = solicitar_input(
            "DNI: ",
            validador=validar_dni,
            error_msg="DNI inválido. Debe tener 8 dígitos.",
        )
        cuenta = solicitar_input(
            "Cuenta bancaria: ",
            validador=validar_cuenta_bancaria,
            error_msg="Cuenta bancaria inválida. Debe tener al menos 10 caracteres.",
        )
        telefono = solicitar_input(
            "Telefono: ",
            validador=validar_telefono,
            error_msg="Telefono inválido. Debe tener 9 dígitos.",
        )
        contrasena = getpass("Contraseña: ")

        def obtener_rol_id():
            if usuario_actual is None:
                return 2
            if (
                hasattr(usuario_actual, "rol")
                and hasattr(usuario_actual.rol, "id_rol")
                and usuario_actual.rol.id_rol == 1
            ):
                rol_id_input = input("Rol (1: Administrador, 2: Usuario): ").strip()
                try:
                    rol_id = int(rol_id_input)
                    if rol_id not in (1, 2):
                        print("ID de rol inválido. Se asigna rol Usuario por defecto.")
                        return 2
                    return rol_id
                except ValueError:
                    print("ID de rol inválido. Se asigna rol Usuario por defecto.")
                    return 2
            print("Solo puedes crear usuarios con rol Usuario.")
            return 2

        rol_id = obtener_rol_id()
        rol = self.rol_repo.obtener_rol_por_id(rol_id)
        if not rol:
            print("Rol no encontrado. Se asigna rol Usuario por defecto.")
            rol = self.rol_repo.obtener_rol_por_id(2)
            if not rol:
                rol = Rol(id_rol=2, nombre="Usuario")

        def obtener_metodo_deposito_id():
            metodos = self.metodo_deposito_repo.obtener_todos_metodos_deposito()
            if not metodos:
                print("No hay métodos de depósito disponibles.")
                return None
            print("Selecciona el método de depósito de tu preferencia:")
            for metodo in metodos:
                print(f"{metodo.id}: {metodo.nombre} - {metodo.descripcion}")
            metodo_id_input = input(
                "Selecciona el método de depósito favorito: "
            ).strip()
            try:
                metodo_id = int(metodo_id_input)
                metodo = self.metodo_deposito_repo.obtener_metodo_deposito_por_id(
                    metodo_id
                )
                if metodo:
                    return metodo.id
                print("Método de depósito no encontrado. Se asigna None.")
            except ValueError:
                print("ID de método de depósito inválido. Se asigna None.")
            return 1

        metodo_deposito_id = obtener_metodo_deposito_id()
        metodo_deposito_fav = None
        if metodo_deposito_id is None:
            print("No se asignará un método de depósito favorito.")
        else:
            metodo_deposito_fav = (
                self.metodo_deposito_repo.obtener_metodo_deposito_por_id(
                    metodo_deposito_id
                )
            )
        if not metodo_deposito_fav:
            print(
                "Método de depósito favorito no encontrado. Se le asignará el primer método disponible."
            )
            metodos = self.metodo_deposito_repo.obtener_todos_metodos_deposito()
            if metodos:
                metodo_deposito_fav = metodos[0]
            else:
                raise ValueError(
                    "No hay métodos de depósito disponibles para asignar al usuario."
                )
        usuario = Usuario(
            nombre=nombre,
            email=email,
            dni=dni,
            cuenta_bancaria=cuenta,
            telefono=telefono,
            metodo_deposito_fav=metodo_deposito_fav,
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
