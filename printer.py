from termcolor import colored
from todo import Todo

import os

def print_todo_list(todo_list: list[Todo]) -> None:
    os.system("clear")
    print_title("ToDo list:")
    for index in range(len(todo_list)):
        if todo_list[index].completed:
            print_completed(todo_list[index])
        else:
            match todo_list[index].priority:
                case 1:
                    print(colored(f"[ ] {index + 1}. {todo_list[index].text}", color="red"))
                case 2:
                    print(colored(f"[ ] {index + 1}. {todo_list[index].text}", color="light_yellow"))
                case 3:
                    print(colored(f"[ ] {index + 1}. {todo_list[index].text}", color="yellow"))

def print_completed(todo: Todo) -> None:
    print(colored(f"[X] - {todo.text}", color="dark_grey", attrs=["strike"]))

def print_title(title: str) -> None:
    print(colored(title, color="light_grey", attrs=["bold", "underline"]))
