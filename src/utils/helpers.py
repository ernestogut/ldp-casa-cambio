def convert_password_to_asterisks(password: str) -> str:
    """
    Convierte una contraseña en una cadena de asteriscos.

    Args:
        password (str): La contraseña original.

    Returns:
        str: Una cadena de asteriscos del mismo largo que la contraseña original.
    """
    return "*" * len(password)
