class Usuario:
    def __init__(self, nombre, email, dni, cuenta_bancaria, contrasena):
        self.nombre = nombre
        self.email = email
        self.dni = dni
        self.cuenta_bancaria = cuenta_bancaria
        self.contrasena = contrasena
        self.transacciones = []

    def agregar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

    def __str__(self):
        return (
            f"Nombre: {self.nombre}, Email: {self.email}, "
            f"DNI: {self.dni}, Cuenta: {self.cuenta_bancaria}"
        )
