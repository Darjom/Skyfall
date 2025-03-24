# permissions/domain/Permission.py

class Permission:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def __eq__(self, other):
        if not isinstance(other, Permission):
            return False
        return self.name == other.name and self.description == other.description