from ..fields import AggregateField


class MatchAggregate(AggregateField[dict[str, any]]):
    def build(self):
        return { "$match" : self.value }
