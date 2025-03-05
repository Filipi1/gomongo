import inspect

from pymongo import MongoClient
from src.repository.dataclass.repository_dataclass import MongoCollection


class InjectRepository:
    def __init__(self, collection: str):
        self.__collection = collection

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            func_params = inspect.signature(func).parameters
            if "repository" in func_params:
                database = MongoClient("mongodb://localhost:27017/").get_database("example")
                kwargs["repository"] = MongoCollection(collection_name="many_entities", database=database)
            func(*args, **kwargs)
        return wrapper