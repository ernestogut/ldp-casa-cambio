import getpass
from models.usuario import Usuario
from models.rol import Rol
from utils.validations import (
    validar_email,
    validar_dni,
    validar_cuenta_bancaria,
)

usuarios = []


def crear_usuario(nombre, email, dni, cuenta_bancaria, contrasena, rol_id, rol_nombre):
    return Usuario(
        nombre, email, dni, cuenta_bancaria, contrasena, Rol(rol_id, rol_nombre)
    )


def registrar_usuario_sistema():
    usuario_sistema = crear_usuario(
        "Sistema",
        "sistema@gmail.com",
        "00000000",
        "0000000000",
        "123456",
        1,
        "Administrador",
    )
    usuarios.append(usuario_sistema)


registrar_usuario_sistema()


def obtener_rol(rol_input):
    roles = {"1": (1, "Administrador"), "2": (2, "Usuario")}
    return roles.get(rol_input, (2, "Usuario"))


def email_existe(email):
    return any(usuario.email == email for usuario in usuarios)


def registrar_usuario():
    print("\n=== Registro de Usuario ===")
    nombre = input("Nombre: ")

    while True:
        email = input("Email: ")
        if not validar_email(email):
            print("Email inválido. Debe contener '@' y un dominio.")
            continue
        if email_existe(email):
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

    contrasena = input("Contraseña: ")
    rol_input = input("Rol (1: Administrador, 2: Usuario): ").strip()
    rol_id, rol_nombre = obtener_rol(rol_input)

    nuevo_usuario = crear_usuario(
        nombre, email, dni, cuenta, contrasena, rol_id, rol_nombre
    )
    usuarios.append(nuevo_usuario)
    print("Usuario registrado con éxito.\n")


def mostrar_usuarios():
    print("\n=== Usuarios Registrados ===")
    if not usuarios or len(usuarios) == 1:
        print("No hay usuarios registrados.")
    else:
        for i, usuario in enumerate(usuarios, start=1):
            if i > 1:
                print(f"{i}. {usuario}")


def iniciar_sesion():
    if not usuarios:
        print("No hay usuarios registrados para iniciar sesión.")
        return None

    print("\n=== Iniciar sesión ===")
    email = input("Email: ")
    contrasena = getpass.getpass("Contraseña: ")

    usuario = next(
        (u for u in usuarios if u.email == email and u.contrasena == contrasena), None
    )
    if usuario:
        print(f"Bienvenido, {usuario.nombre}!\n")
        return usuario

    print("Email o contraseña incorrectos.\n")
    return
