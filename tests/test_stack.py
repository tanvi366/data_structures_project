from dsa.data_structures.stacks import Stack
from dsa.data_structures.queues import Queue
#================================
#  STACK
#================================

def test_stack_starts_empty():
    stack = Stack()
    assert stack.is_empty()

def test_stack_push():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1

def test_stack_is_lifo():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_stack_becomes_empty():
    stack = Stack()

    stack.push(1)
    stack.pop()
    assert stack.is_empty()

def test_pop_empty_stack():
    stack = Stack()
    assert stack.pop() == "Stack empty"

def test_peek_emtpy_stack():
    stack = Stack()
    assert stack.peek() == "Stack empty"

def test_stack_max_capacity():
    stack = Stack()
    for i in range(5):
        stack.push(i)
    assert stack.peek() == 4

def test_stack_max_input_capacity():
    stack = Stack(2)
    for i in range(2):
        stack.push(i)
    assert stack.peek() == 1

def test_full_stack_still_contains_original_items():
    stack = Stack()
    for i in range(5):
        stack.push(i)
    stack.push(5)
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() == 0

def test_push_after_pop_from_full_stack():
    stack = Stack()
    for i in range(5):
        stack.push(i)
    stack.pop()
    stack.push(5)
    assert stack.peek() == 5

def test_peek_does_not_remove_item():
    stack = Stack()
    stack.push(1)

    assert stack.peek() == 1
    assert stack.peek() == 1
    assert stack.pop() == 1

def test_pop_removes_item():
    stack = Stack()
    stack.push(1)
    stack.push(2)

    assert stack.pop() == 2
    assert stack.peek() == 1