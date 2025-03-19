
from  abc import ABC, abstractmethod

from src.roles.domain.Rol import Rol


class RolesRepository(ABC):

    @abstractmethod
    def save(self, role: Rol) -> None:
        pass