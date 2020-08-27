from paragon.module.extensions.abstract_module_extension import AbstractModuleExtension
from paragon.module.module import Module
from paragon.module.properties.property_container import PropertyContainer


class DefaultModuleExtension(AbstractModuleExtension):
    def on_add(self, module: Module, new_entry: PropertyContainer):
        pass

    def on_remove(self, module: Module, target_entry: PropertyContainer):
        pass

    def on_copy(
        self,
        module: Module,
        source_entry: PropertyContainer,
        target_entry: PropertyContainer,
    ):
        pass

    def get_display_name(self, module: Module, entry: PropertyContainer):
        return entry.get_display_name()
