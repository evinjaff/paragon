from paragon.module.extensions.abstract_module_extension import AbstractModuleExtension
from paragon.module.module import Module
from paragon.module.properties.property_container import PropertyContainer


class FE14CharacterModuleExtension(AbstractModuleExtension):
    def on_add(self, module: Module, new_entry: PropertyContainer):
        new_entry["Support ID"].value = 0xFFFF
        new_entry["Parent ID"].value = 0xFFFF
        new_entry["Child ID"].value = 0xFFFF
        new_entry["Support Index"].value = -1

    def on_remove(self, module: Module, target_entry: PropertyContainer):
        pass

    def on_copy(self, module: Module, source_entry: PropertyContainer, target_entry: PropertyContainer):
        target_entry["Support ID"].value = 0xFFFF
        target_entry["Parent ID"].value = 0xFFFF
        target_entry["Child ID"].value = 0xFFFF
        target_entry["Support Index"].value = -1

    def get_display_name(self, module: Module, entry: PropertyContainer):
        return entry.get_display_name()
