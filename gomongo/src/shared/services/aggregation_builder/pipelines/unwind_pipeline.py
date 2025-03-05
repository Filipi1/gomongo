from ..fields import AggregateField


class UnwindAggregate(AggregateField[str]):
    def build(self):
        if isinstance(self.value, str):
            return {"$unwind": self.value if self.value.startswith("$") else f"${self.value}"}

        return {"$unwind": self.value}
