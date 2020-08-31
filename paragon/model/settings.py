from typing import Optional, List

from pydantic import BaseModel

from paragon.model.project import Project


class Settings(BaseModel):
    theme: Optional[str] = None
    remember_last_project: bool = True
    remember_exports: bool = True
    cached_project: int = -1
    projects: List[Project] = []

    def has_cached_project(self) -> bool:
        return self.remember_last_project and self.cached_project in range(
            0, len(self.projects)
        )

    def get_cached_project(self) -> Optional[Project]:
        if not self.has_cached_project():
            return None
        return self.projects[self.cached_project]
