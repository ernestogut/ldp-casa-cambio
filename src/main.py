from src.application.transaccion_service import TransaccionService
from src.application.usuario_service import UsuarioService
from src.infrastructure.in_memory_rol_repository import InMemoryRolRepository
from src.infrastructure.in_memory_usuario_repository import InMemoryUsuarioRepository
from src.infrastructure.in_memory_tasa_cambio_repository import (
    InMemoryTasaCambioRepository,
)
from src.infrastructure.in_memory_transaccion_repository import (
    InMemoryTransaccionRepository,
)
from src.application.tasa_cambio_service import TasaCambioService


usuario_repo = InMemoryUsuarioRepository()
rol_repo = InMemoryRolRepository()
usuario_service = UsuarioService(usuario_repo, rol_repo)
tasa_cambio_repo = InMemoryTasaCambioRepository()
transaccion_repo = InMemoryTransaccionRepository()
tasa_cambio_service = TasaCambioService(tasa_cambio_repo)
transaccion_service = TransaccionService(transaccion_repo, tasa_cambio_service)


def menu_usuario(usuario):
    while True:
        print(f"\n=== Menú Usuario: {usuario.nombre} ===")
        print("1. Cambio de Moneda")
        print("2. Ver mis transacciones")
        print("3. Cerrar sesión")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            transaccion_service.flujo_cambio_divisas(usuario)
        elif opcion == "2":
            transaccion_service.ver_transacciones(usuario)
        elif opcion == "3":
            print(f"Sesión cerrada para {usuario.nombre}.\n")
            break
        else:
            print("Opción no válida.\n")


def menu_admin():
    while True:
        print("\n=== Menú Administrador ===")
        print("1. Registrar usuario")
        print("2. Ver usuarios registrados")
        print("3. Mantenimiento de tasas de cambio")
        print("4. Cerrar sesión")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            usuario_service.registrar_usuario()
        elif opcion == "2":
            usuario_service.mostrar_usuarios()
        elif opcion == "3":
            menu_admin_tasas()
        elif opcion == "4":
            print("Sesión de administrador cerrada.\n")
            break
        else:
            print("Opción no válida.\n")


def menu_admin_tasas():
    while True:
        print("\n--- Mantenimiento de Tasas de Cambio ---")
        print("1. Listar tasas")
        print("2. Agregar tasa")
        print("3. Actualizar tasa")
        print("4. Eliminar tasa")
        print("5. Volver")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            tasas = tasa_cambio_service.listar_tasas()
            for t in tasas:
                print(f"{t.codigo}: {t.nombre} ({t.simbolo}) - Tasa: {t.tasa}")
        elif opcion == "2":
            codigo = input("Código (ejemplo: USD): ").strip()
            nombre = input("Nombre (ejemplo: Dólares): ").strip()
            simbolo = input("Símbolo (ejemplo: $): ").strip()
            try:
                tasa = float(input("Tasa: ").strip())
                tasa_cambio_service.agregar_tasa(codigo, nombre, simbolo, tasa)
                print("Tasa agregada.")
            except ValueError:
                print("Tasa inválida.")
        elif opcion == "3":
            codigo = input("Código a actualizar: ").strip()
            try:
                nueva_tasa = float(input("Nueva tasa: ").strip())
                tasa_cambio_service.actualizar_tasa(codigo, nueva_tasa)
                print("Tasa actualizada.")
            except ValueError:
                print("Tasa inválida.")
        elif opcion == "4":
            codigo = input("Código a eliminar: ").strip()
            tasa_cambio_service.eliminar_tasa(codigo)
            print("Tasa eliminada.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


def main():

    while True:
        print("=== Bienvenido a la Aplicación de Cambio de Divisas ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            usuario_actual = usuario_service.iniciar_sesion()
            if usuario_actual:
                if usuario_actual.rol.slug == "administrador":
                    menu_admin()
                else:
                    menu_usuario(usuario_actual)
        elif opcion == "2":
            usuario_service.registrar_usuario()
        elif opcion == "3":
            print("¡Aplicación terminada!")
            break
        else:
            print("Opción no válida.\n")


if __name__ == "__main__":
    main()
