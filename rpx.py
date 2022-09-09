from pathlib import Path

import click

path_project = Path()
path_component = path_project.absolute()


@click.group()
def rpx():
    pass


@click.command(name="vite")
@click.option("-n", "--name", prompt="Enter name", default="app", help="Name of the application!")
@click.option("-t", "--template", prompt="Enter template", default="react-ts", help="Template of the application! Ex: react-ts (default) or react")
def create_project(name, template):
    from .scripts.cp import c_project
    c_project(name, template)


@click.command(name="component")
def create_component():
    pass


rpx.add_command(create_project)
rpx.add_command(create_component)
