from typing import List, Tuple

from paragon.core.bin_streams import BinArchiveWriter, BinArchiveReader
from paragon.module.module import Module
from paragon.module.properties.property_container import PropertyContainer


class ObjectModule(Module):
    def __init__(self, js):
        super().__init__(js)
        self.element = self.element_template.duplicate(new_owner=self)

    def find_base_address_for_element(self, element):
        if not self.archive:
            raise ValueError
        if element != self.element:
            raise ValueError
        return self.location_strategy.read_base_address(self.archive)

    def attach_to(self, archive):
        location = self.location_strategy.read_base_address(archive)
        reader = BinArchiveReader(archive, location)
        for prop in self.element.values():
            prop.read(reader)
        self.archive = archive

    def commit_changes(self):
        location = self.location_strategy.read_base_address(self.archive)
        writer = BinArchiveWriter(self.archive, location)
        for prop in self.element.values():
            prop.write(writer)

    def _update_post_shallow_copy_fields(self):
        self.element = self.element_template.duplicate(new_owner=self)

    def children(self) -> List[Tuple[PropertyContainer, str, str]]:
        return self.element.children()

    def import_values_from_dict(self, values: dict):
        self.element.import_values(values)
