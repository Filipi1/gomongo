from typing import Dict
from ..fields import AggregateField


class LookupAggregate(AggregateField[Dict[str, any]]):
    def build(self):
        return { "$lookup" : self.value }
