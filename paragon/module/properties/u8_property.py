from PySide2.QtWidgets import QWidget

from paragon.ui.widgets.bitflags_editor import BitflagsEditor
from paragon.ui.widgets.data_combo_box import DataComboBox
from paragon.ui.widgets.integer_property_spin_box import IntegerPropertySpinBox
from .plain_value_property import PlainValueProperty


class U8Property(PlainValueProperty):
    def __init__(self, name, value=0):
        super().__init__(name)
        self.editor_factory = lambda: IntegerPropertySpinBox(self.name, 0, 255)
        self.value = value

    def copy_to(self, destination):
        destination.value = self.value

    @classmethod
    def _from_json(cls, name, json):
        result = U8Property(name)
        result.is_id = json.get("id", False)
        if "editor" in json:
            cls._parse_editor(result, json["editor"])
        return result

    @staticmethod
    def _parse_editor(prop, json):
        editor_type = json["type"]
        if editor_type == "spinbox":
            hex = json.get("hex", False)
            prop.editor_factory = lambda: IntegerPropertySpinBox(prop.name, 0, 255, hex)
        elif editor_type == "combobox":
            data_type = json["data"]
            prop.editor_factory = lambda: DataComboBox(prop.name, data_type, int)
        elif editor_type == "bitflags":
            flags = json["flags"]
            if not type(flags) is list:
                raise TypeError
            prop.editor_factory = lambda: BitflagsEditor(prop.name, flags)

    def read(self, reader):
        self.value = reader.read_u8()

    def write(self, writer):
        writer.write_u8(self.value)

    def create_editor(self) -> QWidget:
        return self.editor_factory()