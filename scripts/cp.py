from os import system


def c_project(name, template):
    cmd = f"yarn create vite {name} --template {template}"
    system(cmd)
