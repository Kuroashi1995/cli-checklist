from file_management import get_todo_list, save_todo_list
from todo import Todo
from printer import print_todo_list


def main():
    todo_list = get_todo_list()
    while (True):
        try:
            print_todo_list(todo_list)
            selection = input("1- Add Todo | 2- Complete Todo | 3- Delete Todo | 4- Clear All | 5- Clear Completed | 6- Order by Priority: > ")
            if selection == "exit":
                break
            elif selection != "":
                match(int(selection)):
                    case 1:
                        text = input("Todo: > ")
                        priority = int(input("Priority 1-3 (default 3): > "))
                        if priority > 3 or priority < 0:
                            priority = 3
                        todo_list.append(Todo(priority, text))
                    case 2:
                        index = int(input("Todo number: > "))
                        if index > len(todo_list):
                            continue
                        todo_list[index - 1].completed = True
                    case 3:
                        index = int(input("Todo number: > "))
                        if index > len(todo_list):
                            continue
                        del todo_list[int(index) - 1]
                    case 4:
                        todo_list = []
                    case 5:
                        todo_list = list(filter(lambda x: not x.completed, todo_list))
                    case 6:
                        def filterer(todo: Todo) -> int | float:
                            if todo.completed:
                                return float("inf")
                            else:
                                return todo.priority
                        todo_list.sort(key=filterer)
                    case _:
                        continue
            save_todo_list(todo_list)
        except ValueError:
            continue
        except KeyboardInterrupt:
            return 1
main()
