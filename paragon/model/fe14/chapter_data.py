import json

from paragon.model.fe14.dispo import Dispo
from paragon.model.fe14.terrain import Terrain
from paragon.model.qt.dispo_model import DisposModel
from paragon.model.qt.tiles_model import TilesModel
from paragon.services.fe14.dialogue_service import Dialogue
from paragon.services.service_locator import locator
from paragon.utils.chapter_utils import (
    detect_route_from_dispo_location,
    search_all_routes_for_file,
    detect_chapter_file_sub_folder,
    search_all_routes_for_file_localized,
)


def _read_dialogue_data():
    elements = []
    with open("Modules/ServiceData/FE14ChapterText.json", "r", encoding="utf-8") as f:
        js = json.load(f)
        for elem in js:
            dialogue = Dialogue(
                elem["name"], elem["path"], elem["key"], elem.get("localized", True)
            )
            elements.append(dialogue)
    return elements


CHAPTER_DIALOGUES = _read_dialogue_data()


def _open_map_config(chapter):
    truncated_cid = chapter["CID"].value[4:]
    target_path = "/map/config/%s.bin" % truncated_cid
    open_files_service = locator.get_scoped("OpenFilesService")
    if not open_files_service.exists(target_path):
        return None
    module_service = locator.get_scoped("ModuleService")
    common_module_service = locator.get_scoped("CommonModuleService")
    module_template = module_service.get_common_module_template("Map Config")
    module = common_module_service.open_common_module(module_template, target_path)
    module_service.set_module_in_use(module)
    return module


def _open_dispos(chapter):
    target_file = "%s.bin.lz" % chapter["CID"].value[4:]
    target_path = search_all_routes_for_file("/GameData/Dispos/", target_file)
    if not target_path:
        return None
    open_files_service = locator.get_scoped("OpenFilesService")
    archive = open_files_service.open(target_path)
    dispos = Dispo()
    dispos.read(archive)
    return dispos


def _open_terrain(chapter):
    target_file = "%s.bin.lz" % chapter["CID"].value[4:]
    target_path = search_all_routes_for_file("/GameData/Terrain/", target_file)
    if not target_path:
        return None
    open_files_service = locator.get_scoped("OpenFilesService")
    archive = open_files_service.open(target_path)
    terrain = Terrain()
    terrain.read(archive)
    return terrain


def _open_person(chapter):
    target_file = "%s.bin.lz" % chapter["CID"].value[4:]
    target_path = search_all_routes_for_file("/GameData/Person/", target_file)
    if not target_path:
        return None
    module_service = locator.get_scoped("ModuleService")
    common_module_service = locator.get_scoped("CommonModuleService")
    module_template = module_service.get_common_module_template("Person")
    module = common_module_service.open_common_module(module_template, target_path)
    module_service.set_module_in_use(module)
    return module


def _open_message_data(chapter):
    cid = chapter["CID"].value
    truncated_cid = cid[4:]
    result = []
    open_files_service = locator.get_scoped("OpenFilesService")
    try:
        for dialogue in CHAPTER_DIALOGUES:
            full_key = dialogue.key % truncated_cid
            message_archive = open_files_service.open_message_archive(
                dialogue.path, localized=dialogue.localized
            )
            if message_archive.has_message(full_key):
                value = message_archive.get_message(full_key)
            else:
                value = ""
            result.append(value)
    except:
        # We only end up here if a message archive cannot be found.
        # Don't bother with message data if the user didn't set things up correctly.
        return None
    return result


def _save_message_data(chapter):
    cid = chapter.chapter["CID"].value
    truncated_cid = cid[4:]
    open_files_service = locator.get_scoped("OpenFilesService")
    for i in range(0, len(CHAPTER_DIALOGUES)):
        dialogue = CHAPTER_DIALOGUES[i]
        full_key = dialogue.key % truncated_cid
        message_archive = open_files_service.open_message_archive(
            dialogue.path, localized=dialogue.localized
        )
        message_archive.insert_or_overwrite_message(full_key, chapter.message_data[i])


def _open_conversation_data(chapter):
    target_file = "%s.bin.lz" % chapter["CID"].value[4:]
    target_path = search_all_routes_for_file_localized("/m/", target_file)
    if not target_path:
        return None
    archive = locator.get_scoped("OpenFilesService").open_message_archive(target_path)
    return archive


class ChapterData:
    def __init__(self, chapter):
        self.chapter = chapter
        self.file_location = detect_route_from_dispo_location(chapter)
        self.config = _open_map_config(chapter)
        self.dispos = _open_dispos(chapter)
        self.terrain = _open_terrain(chapter)
        self.person = _open_person(chapter)
        self.message_data = _open_message_data(chapter)
        self.conversation_data = _open_conversation_data(chapter)

        self.dispos_model = DisposModel(self.dispos, self) if self.dispos else None
        self.tiles_model = TilesModel(self.terrain.tiles) if self.terrain else None

    def save(self):
        open_files_service = locator.get_scoped("OpenFilesService")
        target_file = "%s.bin.lz" % self.chapter["CID"].value[4:]
        if self.dispos:
            suffix = detect_chapter_file_sub_folder(self.chapter) + target_file
            dispos_path = "/GameData/Dispos/" + suffix
            dispos_archive = self.dispos.to_bin()
            open_files_service.register_or_overwrite_archive(
                dispos_path, dispos_archive
            )
        if self.terrain:
            terrain_path = "/GameData/Terrain/" + target_file
            terrain_archive = self.terrain.to_bin()
            open_files_service.register_or_overwrite_archive(
                terrain_path, terrain_archive
            )
        if self.message_data:
            _save_message_data(self)
