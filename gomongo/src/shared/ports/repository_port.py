from abc import ABC, abstractmethod
from typing import Dict, Any, List


class Repository(ABC):
    @abstractmethod
    def find_one(self) -> Dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def find(self) -> List[Dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def update(self) -> Dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def insert(self) -> Dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def delete(self):
        raise NotImplementedError