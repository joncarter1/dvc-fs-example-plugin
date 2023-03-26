"""Dummy FileSystem plugin that simply inherits from LocalFileSystem"""
__all__ = ("DummyFS",)

from dvc_objects.fs.local import LocalFileSystem


class DummyFS(LocalFileSystem):
    protocol = "dummy"

    @classmethod
    def _strip_protocol(cls, path: str) -> str:
        return path.replace("dummy://", "", 1)

    def unstrip_protocol(self, path: str) -> str:
        return f"dummy://{path}"
