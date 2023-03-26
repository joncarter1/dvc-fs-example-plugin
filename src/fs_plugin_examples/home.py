"""Example FileSystem plugin that interprets remote urls as relative to user HOME directory."""
__all__ = ("HomeFS",)

import os
from dvc_objects.fs.local import LocalFileSystem


def _get_home_dir():
    if os.environ.get("HOME") is None:
        raise KeyError("HOME environment variable is unset!")
    return os.environ["HOME"]


class HomeFS(LocalFileSystem):
    protocol = "home"

    @classmethod
    def _strip_protocol(cls, path: str) -> str:
        return os.path.join(_get_home_dir(), path.replace("home://", "", 1))

    def unstrip_protocol(self, path: str) -> str:
        return "home://" + path.replace(_get_home_dir(), "", 1)
