from dataclasses import dataclass
from typing import Optional, List, Dict


@dataclass
class LookupAggregateParams:
    collection_name: str
    local_field: str
    foreign_field: str
    result_field: str
    pipeline: Optional[List[Dict]]

    def to_json(self):
        return {
            "from": self.collection_name,
            "local_field": self.local_field,
            "foreign_field": self.foreign_field,
            "result_field": self.result_field,
            "pipeline": self.pipeline
        }
