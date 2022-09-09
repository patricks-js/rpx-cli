from os import makedirs
from pathlib import Path


def c_files(name: str, path: Path, type: bool):
    if type:
        tsx = path / "index.tsx"
        tsx.touch()
    else:
        jsx = path / "index.jsx"
        jsx.touch()


def c_component(name: str, path: Path, type: bool):
    component_name = name.capitalize()
    # component_path = f"{path}/src/components/{component_name}"
    component_path = path / "src" / "components" / component_name
    makedirs(component_path)
    c_files(component_name, component_path, type)
