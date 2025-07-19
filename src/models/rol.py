class Rol:
    def __init__(self, id_rol, nombre):
        self.id_rol = id_rol
        self.nombre = nombre
        self.slug = nombre.lower().replace(" ", "-")

    def __repr__(self):
        return f"Rol(id_rol={self.id_rol}, nombre='{self.nombre}')"

    def __eq__(self, other):
        if not isinstance(other, Rol):
            return False
        return self.id_rol == other.id_rol and self.nombre == other.nombre
