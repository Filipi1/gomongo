from ..fields import AggregateField


class InjectionAggregate(AggregateField[list[dict]]):
    def build(self):
        return self.value
