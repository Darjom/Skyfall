# src/roles/domain/Rol.py

class Rol:
    """
    Entidad de dominio pura (sin SQLAlchemy).
    """
    def __init__(self, name: str, description: str = ""):
        self._name = name
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def can_edit(self):
        # Ejemplo de lógica de dominio
        return self._name == "superuser"