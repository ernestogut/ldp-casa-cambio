from models.usuario import Usuario

usuarios = []


def registrar_usuario():
    print("\n=== Registro de Usuario ===")
    nombre = input("Nombre: ")
    email = input("Email: ")
    dni = input("DNI: ")
    cuenta = input("Cuenta bancaria: ")
    contrasena = input("Contraseña: ")

    for usuario in usuarios:
        if usuario.email == email:
            print("Este email ya está registrado. Usa otro.")
            return

    nuevo_usuario = Usuario(nombre, email, dni, cuenta, contrasena)
    usuarios.append(nuevo_usuario)
    print("Usuario registrado con éxito.\n")


def mostrar_usuarios():
    print("\n=== Usuarios Registrados ===")
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario}")


def iniciar_sesion():
    if not usuarios:
        print("No hay usuarios registrados para iniciar sesión.")
        return None

    print("\n=== Iniciar sesión ===")
    email = input("Email: ")
    contrasena = input("Contraseña: ")

    for usuario in usuarios:
        if usuario.email == email and usuario.contrasena == contrasena:
            print(f"Bienvenido, {usuario.nombre}!\n")
            return usuario

    print("Email o contraseña incorrectos.\n")
    return None
