def validar_monto_positivo(monto: float) -> bool:
    if monto <= 0:
        return False
    return True


def validar_moneda(moneda: str, opciones: list) -> bool:
    if moneda not in opciones:
        return False
    return True


def validar_monto_origen_destino(monto_origen: float, monto_destino: float) -> bool:
    if monto_origen <= 0 or monto_destino <= 0:
        return False
    return True


def validar_email(email: str) -> bool:
    return "@" in email and "." in email


def validar_dni(dni: str) -> bool:
    if len(dni) != 8 or not dni.isdigit():
        return False
    return True


def validar_cuenta_bancaria(cuenta_bancaria: str) -> bool:
    if len(cuenta_bancaria) < 10:
        return False
    return True


def email_existe(email, usuarios) -> bool:
    return any(usuario.email == email for usuario in usuarios)
