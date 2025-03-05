from ..fields import AggregateField


class SkipAggregate(AggregateField[int]):
    def build(self):
        return { "$skip" : self.value }
