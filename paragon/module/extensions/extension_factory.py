from typing import Optional

from paragon.module.extensions.abstract_module_extension import AbstractModuleExtension
from paragon.module.extensions.default_module_extension import DefaultModuleExtension
from paragon.module.extensions.fe14_character_module_extension import FE14CharacterModuleExtension
from paragon.module.extensions.fe14_person_module_extension import FE14PersonModuleExtension

_EXTENSIONS = {
    "fe14_character": FE14CharacterModuleExtension(),
    "fe14_person": FE14PersonModuleExtension()
}


def get_extension_from_string(extension_name: Optional[str]) -> AbstractModuleExtension:
    if extension_name in _EXTENSIONS:
        return _EXTENSIONS[extension_name]
    else:
        return DefaultModuleExtension()
