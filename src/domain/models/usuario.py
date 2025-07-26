from .rol import Rol
from .transaccion import Transaccion
from src.utils.validations import validar_email, validar_dni, validar_cuenta_bancaria
from .metodo_deposito import MetodoDeposito

_usuario_id_counter = 1


def id_generator():
    global _usuario_id_counter
    id_actual = _usuario_id_counter
    _usuario_id_counter += 1
    return id_actual


class Usuario:
    def __init__(
        self,
        nombre: str,
        email: str,
        dni: str,
        cuenta_bancaria: str,
        telefono: str,
        metodo_deposito_fav: MetodoDeposito,
        contrasena: str,
        rol: Rol,
    ):
        self.id = id_generator()
        self.nombre = nombre
        self.email = email
        self.dni = dni
        self.cuenta_bancaria = cuenta_bancaria
        self.telefono = telefono
        self.metodo_deposito_fav = metodo_deposito_fav
        self.contrasena = contrasena
        self.transacciones = []
        self.rol = rol

    def agregar_transaccion(self, transaccion: Transaccion):
        self.transacciones.append(transaccion)

    def __str__(self):
        return (
            f"Nombre: {self.nombre}, Email: {self.email}, "
            f"DNI: {self.dni}, Cuenta: {self.cuenta_bancaria}, Teléfono: {self.telefono}, Rol: {self.rol.nombre}, "
            f"Método de Depósito Favorito: {self.metodo_deposito_fav.nombre if self.metodo_deposito_fav else 'No asignado'}"
        )
