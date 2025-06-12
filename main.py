from file_management import get_todo_list, save_todo_list
from todo import Todo
from printer import print_todo_list


def main():
    todo_list = get_todo_list()
    while (True):
        try:
            print_todo_list(todo_list)
            user_input = input("Enter new todo | Enter todo number | order | clear | exit: > ")
            # Check for exit
            if user_input == "exit":
                break
            # Check for order
            elif user_input == "order":
                def filterer(todo: Todo) -> int | float:
                    if todo.completed:
                        return float("inf")
                    else:
                        return todo.priority
                todo_list.sort(key=filterer)
            #Check for clear
            elif user_input == "clear":
                option = int(input("1. Clear All | 2. Clear completed: > "))
                match(option):
                    case 1:
                        todo_list = []
                    case 2:
                        todo_list = list(filter(lambda x: not x.completed, todo_list))
            #Check for existing input
            elif user_input != "":
                #Check that is a valid todo
                try:
                    if int(user_input) > 0 and int(user_input) <= len(todo_list):
                        index = int(user_input)
                        option = int(input("1. Complete Todo | 2. Delete Todo | 3. Edit Todo: > "))
                        #Check for valid options
                        match(option):
                            case 1:
                                todo_list[index - 1].completed = True
                            case 2:
                                del todo_list[index - 1]
                            case 3:
                                new_text = input(f"New description (old '{todo_list[index - 1].text})' > ")
                                # Check that priority is correct
                                while True:
                                    new_priority = int(input(f"New priority (old '{todo_list[index - 1].priority}') > "))
                                    if new_priority > 0 and new_priority <= 3:
                                        break
                                #update todo
                                todo_list[index - 1].text = new_text
                                todo_list[index - 1].priority = new_priority
                        continue
                except ValueError:
                    print("Adding new Todo:")
                text = user_input
                while True:
                    priority = int(input("Priority: 1-3: > "))
                    if priority > 0 and priority <= 3:
                        break
                todo_list.append(Todo(priority, text))
            save_todo_list(todo_list)
        except KeyboardInterrupt:
            return 1
main()
