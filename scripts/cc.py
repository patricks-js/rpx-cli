from os import makedirs
from pathlib import Path


def write_file(name: str, file: Path):
    with file.open("a+") as fw:
        fw.write("// import * as S from './styles';\n\n")
        fw.write(f"export const {name} = () => {{\n")
        fw.write("  return (\n")
        fw.write("      <div>\n")
        fw.write("      </div>\n")
        fw.write("  )\n")
        fw.write("}\n")


def c_files(name: str, path: Path, suffix: str):
    file = path / f"index.{suffix}"
    file.touch()
    write_file(name, file)


def c_component(name: str, path: Path, suffix: str):
    component_name = name.capitalize()
    # component_path = f"{path}/src/components/{component_name}"
    component_path = path / "src" / "components" / component_name
    makedirs(component_path)
    c_files(component_name, component_path, suffix)
