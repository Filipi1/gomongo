from abc import ABC, abstractmethod
from .entity_port import Entity


class Repository[T: Entity](ABC):
    @abstractmethod
    def find_one(self) -> T:
        raise NotImplementedError

    @abstractmethod
    def find(self) -> T:
        raise NotImplementedError

    @abstractmethod
    def update(self) -> T:
        raise NotImplementedError

    @abstractmethod
    def insert(self) -> T:
        raise NotImplementedError

    @abstractmethod
    def delete(self) -> T:
        raise NotImplementedError