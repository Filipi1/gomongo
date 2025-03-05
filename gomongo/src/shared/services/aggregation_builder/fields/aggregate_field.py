from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

T = TypeVar("T")
class AggregateField(ABC, Generic[T]):
    value: Optional[T]

    def __init__(self, value: T):
        self.value = value
        super().__init__()

    @abstractmethod
    def build(self) -> dict:
        raise NotImplementedError("Should implement a 'build' to mongo aggregation.")

    def is_empty(self) -> bool:
        if isinstance(self.value, int):
            return False

        return not self.value
