from PySide2.QtWidgets import QWidget

from paragon.ui.widgets.string_property_line_edit import StringPropertyLineEdit
from .plain_value_property import PlainValueProperty


class MappedProperty(PlainValueProperty):
    def __init__(self, name, value=None):
        super().__init__(name)
        self.editor_factory = lambda: StringPropertyLineEdit(self.name)
        self.value = value
        self.old_values = []

    def copy_to(self, destination):
        destination.value = self.value

    def set_value(self, new_value, follow_link=True):
        self.old_values.append(self.value)
        self.value = new_value
        if self.linked_property and follow_link:
            linked_property = self.parent[self.linked_property]
            linked_property.set_value(self.value, follow_link=False)

    @classmethod
    def _from_json(cls, name, json):
        result = MappedProperty(name)
        result.is_key = json.get("key", False)
        result.is_display = json.get("display", False)
        result.is_fallback_display = json.get("fallback_display", False)
        result.linked_property = json.get("linked_property", None)
        return result

    def read(self, reader):
        self.value = reader.read_mapped()

    def write(self, writer):
        archive = writer.archive
        for old_value in self.old_values:
            archive.clear_mapped_pointer(writer.tell(), old_value)
        self.old_values.clear()
        writer.write_mapped(self.value)

    def create_editor(self) -> QWidget:
        return self.editor_factory()
