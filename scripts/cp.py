from os import system


def c_project(name, template, style):
    create = f"yarn create vite {name} --template {template} || npm init vite@latest {name} -- --template {template}"
    delete_files = f"cd {name} && rm -r public && cd src && unlink App.css && cd assets && unlink react.svg"
    if style == "tailwindcss":
        initialize = f"cd {name} && yarn || npm install && yarn add -D {style} postcss autoprefixer || npm install -D {style} postcss autoprefixer && npx tailwindcss init"
    else:
        if template == "react-ts":
            initialize = f"cd {name} && yarn || npm install && yarn add {style} @types/{style} || npm install {style} @types/{style}"
        else:
            initialize = f"cd {name} && yarn || npm install && yarn add {style} || npm install {style}"

    system(create)
    system(delete_files)
    system(initialize)
