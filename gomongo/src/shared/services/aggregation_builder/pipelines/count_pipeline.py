from ..fields import AggregateField


class CountAggregate(AggregateField[str]):
    def build(self):
        return {"$count": self.value}
