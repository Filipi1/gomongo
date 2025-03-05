from ..fields import AggregateField


class SortAggregate(AggregateField[dict[str, any]]):
    def build(self):
        return {"$sort": self.value}
