from unittest import TestCase
from file_management import get_todo_list, save_todo_list
from todo import Todo

import os

class TestFileManagement(TestCase):
    def test_get_todos_no_file(self):
        todos = get_todo_list("./example.txt")
        self.assertEqual(todos, [])

    def test_get_todos_file(self):
        with open("./example.txt", "w") as example:
            example.write("1:::Example:::False")
        todos = get_todo_list("./example.txt")
        self.assertEqual(todos, [Todo(1, "Example")])
        os.remove("./example.txt")

    def test_get_todos_wrong(self):
        with open("./example.txt", "w") as example:
            example.write("bad example")
        todos = get_todo_list("./example.txt")
        self.assertEqual(todos, [])
        os.remove("./example.txt")

    def test_save_file(self):
        save_todo_list([Todo(1, "Testing")], "./example.txt")
        check = os.path.isfile("./example.txt")
        self.assertEqual(check, True)
        os.remove("./example.txt")
