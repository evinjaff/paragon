from abc import ABC, abstractmethod

from paragon.module.module import Module
from paragon.module.properties.property_container import PropertyContainer


class AbstractModuleExtension(ABC):
    @abstractmethod
    def on_add(self, module: Module, new_entry: PropertyContainer):
        pass

    @abstractmethod
    def on_remove(self, module: Module, target_entry: PropertyContainer):
        pass

    @abstractmethod
    def on_copy(
        self,
        module: Module,
        source_entry: PropertyContainer,
        target_entry: PropertyContainer,
    ):
        pass

    @abstractmethod
    def get_display_name(self, module: Module, entry: PropertyContainer):
        pass
