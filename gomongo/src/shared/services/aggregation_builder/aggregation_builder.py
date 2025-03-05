from typing import Dict, List, Optional

from .dataclasses import LookupAggregateParams
from .fields import AggregateField
from .pipelines import (
    AddFieldsAggregate,
    CountAggregate,
    InjectionAggregate,
    LimitAggregate,
    LookupAggregate,
    MatchAggregate,
    ProjectAggregate,
    SkipAggregate,
    SortAggregate,
    UnwindAggregate,
)


class MongoAggregateBuilder:
    _aggregations: list[AggregateField] = []

    def __init__(self):
        self._aggregations = []

    def match(self, query: dict[str, any]) -> "MongoAggregateBuilder":
        self._aggregations.append(MatchAggregate(value=query))
        return self

    def sort(self, query: dict[str, any]) -> "MongoAggregateBuilder":
        self._aggregations.append(SortAggregate(value=query))
        return self

    def lookup(
        self,
        collection_name: str,
        local_field: str,
        foreign_field: str,
        result_field_name: str,
        pipeline: Optional[List[Dict]] = None,
    ) -> "MongoAggregateBuilder":
        data = {
            "collection_name": collection_name,
            "local_field": local_field,
            "foreign_field": foreign_field,
            "result_field_name": result_field_name,
        }

        if pipeline:
            data["pipeline"] = pipeline  # type: ignore

        valid_dict = LookupAggregateParams(**data).to_json()
        self._aggregations.append(LookupAggregate(value=valid_dict))
        return self

    def unwind(self, field_name: str) -> "MongoAggregateBuilder":
        self._aggregations.append(UnwindAggregate(value=field_name))
        return self

    def skip(self, quantity: int) -> "MongoAggregateBuilder":
        self._aggregations.append(SkipAggregate(value=quantity))
        return self

    def limit(self, quantity: int) -> "MongoAggregateBuilder":
        self._aggregations.append(LimitAggregate(value=quantity))
        return self

    def project(self, query: dict[str, any]) -> "MongoAggregateBuilder":
        self._aggregations.append(ProjectAggregate(value=query))
        return self

    def count(self, field_name: str) -> "MongoAggregateBuilder":
        self._aggregations.append(CountAggregate(value=field_name))
        return self

    def add_fields(self, query: dict[str, any]) -> "MongoAggregateBuilder":
        self._aggregations.append(AddFieldsAggregate(value=query))
        return self

    def inject(self, data: list[dict[str, any]]) -> "MongoAggregateBuilder":
        self._aggregations.append(InjectionAggregate(value=data))
        return self

    def build(self) -> list[dict]:
        result: list[dict] = []
        for aggregation in self._aggregations:
            if aggregation.is_empty():
                continue

            if isinstance(aggregation.value, list):
                result.extend(aggregation.value)
                continue

            result.append(aggregation.build())
        return result
