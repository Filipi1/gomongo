from ..fields import AggregateField


class AddFieldsAggregate(AggregateField[dict[str, any]]):
    def build(self):
        return {"$addFields": self.value}
