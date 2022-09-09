from pathlib import Path

import click

path_project = Path()
# path_component = path_project.absolute()

help_op = {
    "help": [
        "Name of the application!",
        "Template of the application! Ex: react-ts (default) or react",
        "Style of the application! Ex: styled-components (default) or tailwindcss"
    ]
}


@click.group()
def rpx():
    pass


@click.command(name="vite")
@click.option(
    "-n",
    "--name",
    prompt="Enter name",
    default="app",
    help=help_op["help"][0]
)
@click.option(
    "-t",
    "--template",
    prompt="Enter template",
    default="react-ts",
    help=help_op["help"][1]
)
@click.option(
    "-s",
    "--style",
    prompt="Enter type style",
    default="styled-components",
    help=help_op["help"][2]
)
def create_project(name, template, style):
    from scripts.cp import c_project
    c_project(name, template, style)


@click.command(name="component")
@click.option("-n", "--name", prompt="Enter component name", help="Name of the component")
def create_component(name):
    from scripts.cc import c_component
    is_tsx = True if f"{path_project}/src/main.tsx" else False
    c_component(name, path_project, is_tsx)


rpx.add_command(create_project)
rpx.add_command(create_component)
