from ..fields import AggregateField


class LimitAggregate(AggregateField[int]):
    def build(self):
        return {"$limit": self.value}
