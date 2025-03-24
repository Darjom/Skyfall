class User:
    def __init__(self, id: int, first_name: str, last_name: str, email: str, password: str, active: bool):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.active = active

    def has_role(self, role_name: str) -> bool:
        # Lógica para verificar si el usuario tiene un rol específico
        pass