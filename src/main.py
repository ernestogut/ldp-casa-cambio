from services.usuario_service import registrar_usuario, mostrar_usuarios, iniciar_sesion
from services.transaccion_service import flujo_cambio_divisas, ver_transacciones


def menu_usuario(usuario):
    while True:
        print(f"\n=== Menú Usuario: {usuario.nombre} ===")
        print("1. Cambiar dólares a soles")
        print("2. Ver mis transacciones")
        print("3. Cerrar sesión")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            flujo_cambio_divisas(usuario)
        elif opcion == "2":
            ver_transacciones(usuario)
        elif opcion == "3":
            print(f"Sesión cerrada para {usuario.nombre}.\n")
            break
        else:
            print("Opción no válida.\n")


def main():
    while True:
        print("=== Aplicación de Cambio de Divisas ===")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Iniciar sesión")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            usuario_actual = iniciar_sesion()
            if usuario_actual:
                menu_usuario(usuario_actual)
        elif opcion == "4":
            print("Aplicación terminada!")
            break
        else:
            print("Opción no válida.\n")


if __name__ == "__main__":
    main()
