### Example DVC FileSystem plugin

This repository contains examples of DVC FileSystem plugins.

Custom implementations can enable users to implement their own custom FileSystems beyond the currently supported
examples.

After pip installing the plugin package, the 'dummy' and 'home' URI schemes are exposed to DVC:
- `dummy` - mirrors the functionality of LocalFileSystem.
- `home` - implements a remote store whose path is defined relative to a user's home directory.

This is done using entrypoints (see `src/setup.py`)

n.b. this currrently relies on the following experimental branches:

- dvc: https://github.com/joncarter1/dvc/tree/filesystem-plugin
- dvc-objects: https://github.com/joncarter1/dvc-objects/tree/filesystem-plugin