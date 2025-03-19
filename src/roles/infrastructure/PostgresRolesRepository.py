from src.roles.domain.Rol import Rol
from src.roles.domain.RolesRepository import RolesRepository

class PostgresRolesRepository(RolesRepository):

    def __init__(self):
        pass

    def save(self, role: Rol) -> None:
        from src.roles.infrastructure.persistence.RolMapping import RolMapping
        role_mapping = RolMapping.from_domain(role)
        role_mapping.add(role_mapping)
        role_mapping.commit()
        role_mapping.flush()
