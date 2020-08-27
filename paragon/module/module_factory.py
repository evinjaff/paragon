import logging
from json import load

from paragon.module.module import Module
from paragon.module.object_module import ObjectModule
from paragon.module.table_module import TableModule


def create_module_from_path(path) -> Module:
    with open(path, "r", encoding="utf-8") as f:
        js = load(f)
        if js["type"] == "table":
            return TableModule(js)
        elif js["type"] == "object":
            return ObjectModule(js)
        else:
            logging.error("Unrecognized module type. Aborting module creation.")
            raise NotImplementedError
