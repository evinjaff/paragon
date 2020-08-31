import json
import logging
from typing import Optional

from paragon.model.project import Project
from paragon.model.qt.project_model import ProjectModel
from paragon.model.settings import Settings


class SettingsService:
    def __init__(self):
        logging.info("Loading settings from disk.")
        try:
            with open("paragon.json", "r", encoding="utf-8") as f:
                js = json.load(f)
                self.settings = Settings(**js)
            logging.info("Successfully loaded settings from disk.")
        except:
            logging.exception("Unable to load settings. Using defaults.")
            self.settings = Settings()
        self.project_model = ProjectModel(self.settings.projects)

    def save_settings(self):
        logging.info("Saving settings.")
        try:
            with open("paragon.json", "w", encoding="utf-8") as f:
                f.write(self.settings.json(indent=4, ensure_ascii=False))
            logging.info("Successfully wrote settings to disk.")
        except:
            logging.exception("Unable to write settings to disk.")

    def save(self, project):
        self.settings.cached_project = self.project_model.projects.index(project)
        self.save_settings()

    def get_cached_project(self) -> Optional[Project]:
        return self.settings.get_cached_project()

    def has_cached_project(self) -> bool:
        return self.settings.has_cached_project()

    def get_theme(self) -> Optional[str]:
        return self.settings.theme

    def set_theme(self, theme: Optional[str]):
        self.settings.theme = theme

    def get_project_model(self) -> ProjectModel:
        return ProjectModel(self.settings.projects)

    def should_remember_last_project(self) -> bool:
        return self.settings.remember_last_project

    def set_remember_last_project(self, remember_last_project: bool):
        self.settings.remember_last_project = remember_last_project

    def get_remember_exports(self) -> bool:
        return self.settings.remember_exports

    def set_remember_exports(self, new_value: bool):
        self.settings.remember_exports = new_value
