class Node:
    value: int = 0
    prev: "Node | None"

    def __init__(self, value: int, prev: "Node | None"):
        self.value = value
        self.prev = prev

class Stack:
    current: Node | None
    minimum: Node | None
    size: int

    def __init__(self):
        self.current = None
        self.minimum = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.size <= 0

    def peek(self) -> int:
        self.check_size()
        return self.current.value

    def pop(self) -> int:
        self.check_size()
        value = self.current.value
        self.current = self.current.prev
        self.minimum = self.minimum.prev
        self.size -= 1
        return value

    def push(self, value: int) -> None:
        new_node = Node(value, self.current)

        self.minimum = Node(value, self.minimum)
        if self.minimum.prev is not None and self.minimum.prev.value < value:
            self.minimum.value = self.minimum.prev.value

        self.current = new_node
        self.size += 1

    def min(self) -> int:
        self.check_size()
        return self.minimum.value

    def check_size(self) -> None:
        if self.size <= 0:
            raise IndexError("Stack is empty")