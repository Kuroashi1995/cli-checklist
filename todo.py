class Todo:
    def __init__(self, priority: int, text: str, completed: bool = False) -> None:
        self.priority = priority
        self.text = text
        self.completed = completed

    def complete_todo(self):
        self.completed = True

    def __eq__(self, other ) -> bool:
        if not isinstance(other, Todo):
            return False
        return (
                self.completed == other.completed and
                self.priority == other.priority and
                self.text == other.text
                )
