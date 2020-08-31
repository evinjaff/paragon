from enum import Enum

import fefeditor2
from pydantic import BaseModel


class Game(Enum):
    FE13 = 0
    FE14 = 1
    FE15 = 2


class Language(Enum):
    ENGLISH_NA = 0
    ENGLISH_EU = 1
    JAPANESE = 2
    FRENCH = 3
    SPANISH = 4
    GERMAN = 5
    ITALIAN = 6


class Project(BaseModel):
    name: str
    rom_path: str
    output_path: str
    game: Game
    language: Language
    export_selections: dict = {}
    metadata: dict = {}

    def get_filesystem(self):
        if self.game == Game.FE13:
            return fefeditor2.create_fe13_file_system(
                self.rom_path, self.output_path, self.language.value
            )
        elif self.game == Game.FE14:
            return fefeditor2.create_fe14_file_system(
                self.rom_path, self.output_path, self.language.value
            )
        else:
            return fefeditor2.create_fe15_file_system(
                self.rom_path, self.output_path, self.language.value
            )

    def get_language_name(self):
        return Language(self.language).name

    def get_game_name(self):
        return Game(self.game).name

    def get_module_dir(self):
        return "Modules/%s/" % Game(self.game).name
