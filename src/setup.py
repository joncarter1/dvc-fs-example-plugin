from setuptools import find_packages, setup

setup(
    name="dvc-dummy-plugin",
    version="0.1",
    author="Jonathan Carter",
    description="Dummy DVC file system plugin",
    packages=find_packages(include=["fs_plugin_examples"]),
    entry_points={
        "dvc_objects.fs_plugins": [
            "home=fs_plugin_examples.home.HomeFS",
            "dummy=fs_plugin_examples.dummy.DummyFS",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
