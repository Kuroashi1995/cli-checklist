from todo import Todo

import os


def get_todo_list(path: str = "./todos.txt") -> list[Todo]:
    todo_list = []
    try:
        list_file_exists = os.path.isfile(path)
        if list_file_exists:
            with open(path) as f:
                content = f.read()
                lines = content.split("\n")
                lines = list(filter(None, lines))
                for line in lines:
                    data = line.split(":::")
                    todo_list.append(Todo(int(data[0]), data[1], data[2] == "true"))
        return todo_list
    except ValueError:
        return todo_list

def save_todo_list(todo_list: list[Todo], path: str = "./todos.txt") -> None:
    save = ""
    for todo in todo_list:
        save += f"{todo.priority}:::{todo.text}:::{todo.completed}\n"
    with open(path, "w") as f:
        f.write(save)
