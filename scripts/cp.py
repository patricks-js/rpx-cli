from os import system


def c_project(name, template, style):
    create = f"yarn create vite {name} --template {template}"
    if style == "tailwindcss":
        initialize = f"cd {name} && yarn && yarn add -D {style} postcss autoprefixer && npx tailwindcss init"
    else:
        if template == "react-ts":
            initialize = f"cd {name} && yarn && yarn add {style} @types/{style}"
        else:
            initialize = f"cd {name} && yarn && yarn add {style}"

    system(create)
    system(initialize)
