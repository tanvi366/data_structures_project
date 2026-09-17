class Stack:
    """Represent a stack using last-in, first-out (LIFO) order."""
    def __init__(self, max = 5):
        self.items = []
        #points to last item in stack
        self.pointer = -1
        self.max = max

    def push(self,item):
        """Add an item to top of stack"""
        if self.pointer+1 == self.max:
            return "Stack Full"
        else:
            self.items.append(item)
            self.pointer += 1

    def pop(self):
        """Remove and return the item at the top of the stack."""
        if self.pointer == -1:
            return "Stack empty"
        else:
            item = self.items.pop()
            self.pointer -= 1
            return item

    def peek(self):
        """Return the item at the top of the stack without removing."""
        if self.pointer == -1:
            return "Stack empty"
        return self.items[self.pointer]

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        if self.pointer == -1:
            return True
        else:
            return False