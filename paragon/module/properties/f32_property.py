from PySide2.QtWidgets import QWidget

from paragon.ui.widgets.f32_property_spin_box import DoublePropertySpinBox
from .plain_value_property import PlainValueProperty


class F32Property(PlainValueProperty):
    def __init__(self, name, value=0):
        super().__init__(name)
        self.value = value

    def copy_to(self, destination):
        destination.value = self.value

    @classmethod
    def _from_json(cls, name, _json):
        return F32Property(name)

    def read(self, reader):
        self.value = reader.read_f32()

    def write(self, writer):
        writer.write_f32(self.value)

    def create_editor(self) -> QWidget:
        return DoublePropertySpinBox(self.name)
