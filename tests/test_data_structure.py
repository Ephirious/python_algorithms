from src.data_structure.stack import Stack

import pytest

@pytest.fixture
def empty_stack():
    return Stack()

@pytest.fixture
def populated_stack():
    s = Stack()
    s.push(10)
    s.push(5)
    s.push(20)
    s.push(2)
    return s

def test_stack_is_initially_empty(empty_stack):
    assert empty_stack.is_empty() is True
    assert empty_stack.size == 0
    assert empty_stack.current is None
    assert empty_stack.minimum is None


@pytest.mark.parametrize("pushed, minimum, current_size", [
    ([10], 10, 1),
    ([10, 5], 5, 2),
    ([5, 10], 5, 2),
    ([5, 10, 2, 50, 1], 1, 5),
    ([-1, -100, 5], -100, 3),
])
def test_push_and_min_operations(empty_stack, pushed, minimum, current_size):
    """Тестирует корректность работы push, size и min при добавлении разных наборов значений."""
    s = empty_stack
    for val in pushed:
        s.push(val)

    assert s.size == current_size
    assert s.min() == minimum
    assert s.peek() == pushed[-1]

def test_pop_operations(populated_stack):
    s = populated_stack

    assert s.size == 4
    assert s.min() == 2
    assert s.pop() == 2

    assert s.size == 3
    assert s.min() == 5
    assert s.pop() == 20

    assert s.size == 2
    assert s.min() == 5
    assert s.pop() == 5

    assert s.size == 1
    assert s.min() == 10
    assert s.pop() == 10

    assert s.is_empty()

def test_pop_on_empty_stack_raises_index_error(empty_stack):
    with pytest.raises(IndexError, match="Stack is empty"):
        empty_stack.pop()

def test_peek_on_empty_stack_raises_index_error(empty_stack):
    with pytest.raises(IndexError, match="Stack is empty"):
        empty_stack.peek()

def test_min_on_empty_stack_raises_index_error(empty_stack):
    with pytest.raises(IndexError, match="Stack is empty"):
        empty_stack.min()