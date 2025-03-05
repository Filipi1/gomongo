from ..fields import AggregateField


class ProjectAggregate(AggregateField[dict[str, any]]):
    def build(self):
        return {"$project": self.value}
