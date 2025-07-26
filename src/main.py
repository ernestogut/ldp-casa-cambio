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
from src.infrastructure.in_memory_metodo_deposito import (
    InMemoryMetodoDepositoRepository,
)
from src.application.tasa_cambio_service import TasaCambioService


usuario_repo = InMemoryUsuarioRepository()
rol_repo = InMemoryRolRepository()
metodo_deposito_repo = InMemoryMetodoDepositoRepository()
usuario_service = UsuarioService(usuario_repo, rol_repo, metodo_deposito_repo)
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


def menu_admin(usuario_actual):
    while True:
        print("\n=== Menú Administrador ===")
        print("1. Cambio de Moneda")
        print("2. Ver mis transacciones")
        print("3. Registrar usuario")
        print("4. Ver usuarios registrados")
        print("5. Mantenimiento de divisas")
        print("6. Cerrar sesión")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            transaccion_service.flujo_cambio_divisas(usuario_actual)
        elif opcion == "2":
            transaccion_service.ver_transacciones(usuario_actual)
        elif opcion == "3":
            usuario_service.registrar_usuario(usuario_actual)
        elif opcion == "4":
            usuario_service.mostrar_usuarios()
        elif opcion == "5":
            menu_admin_divisas()
        elif opcion == "6":
            print("Sesión de administrador cerrada.\n")
            break
        else:
            print("Opción no válida.\n")


def menu_admin_divisas():
    while True:
        print("\n--- Mantenimiento de Divisas ---")
        print("1. Listar divisas")
        print("2. Agregar divisa")
        print("3. Actualizar divisa")
        print("4. Eliminar divisa")
        print("5. Volver")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            tasas = tasa_cambio_service.listar_tasas()
            for t in tasas:
                print(
                    f"{t.moneda_origen.codigo}->{t.moneda_destino.codigo}: {t.moneda_origen.nombre} ({t.moneda_origen.simbolo}) -> {t.moneda_destino.nombre} ({t.moneda_destino.simbolo}) - Tasa: {t.tasa}"
                )
        elif opcion == "2":
            print("Datos de moneda origen:")
            cod_origen = input("Código: ").strip()
            nom_origen = input("Nombre: ").strip()
            sim_origen = input("Símbolo: ").strip()
            print("Datos de moneda destino:")
            cod_destino = input("Código: ").strip()
            nom_destino = input("Nombre: ").strip()
            sim_destino = input("Símbolo: ").strip()
            try:
                tasa = float(input("Tasa: ").strip())
                tasa_cambio_service.agregar_tasa(
                    cod_origen,
                    nom_origen,
                    sim_origen,
                    cod_destino,
                    nom_destino,
                    sim_destino,
                    tasa,
                )
                print("Tasa agregada.")
            except ValueError:
                print("Tasa inválida.")
        elif opcion == "3":
            key = input("Clave de tasa a actualizar (ejemplo: USD->PEN): ").strip()
            try:
                nueva_tasa = float(input("Nueva tasa: ").strip())
                tasa_cambio_service.actualizar_tasa(key, nueva_tasa)
                print("Tasa actualizada.")
            except ValueError:
                print("Tasa inválida.")
        elif opcion == "4":
            key = input("Clave de tasa a eliminar (ejemplo: USD->PEN): ").strip()
            tasa_cambio_service.eliminar_tasa(key)
            print("Tasa eliminada.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida.\n")


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
                    menu_admin(usuario_actual)
                else:
                    menu_usuario(usuario_actual)
        elif opcion == "2":
            usuario_service.registrar_usuario(None)
        elif opcion == "3":
            print("¡Aplicación terminada!")
            break
        else:
            print("Opción no válida.\n")


if __name__ == "__main__":
    main()
