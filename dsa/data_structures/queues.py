class Queue:
    """Represent a queue using first-in, first-out (FIFO) order."""
    def __init__(self, max = 5):
        self.items = []
        # fp [ x, x, x] bp
        self.fp = 0 # next item to remove
        self.bp = 0 # next item to insert
        self.max = max
        self.count = 0

    def enqueue(self,item):
        """Add an item to the back of the queue."""
        if self.bp == self.max:
            return "Queue Full"
        self.items.append(item)
        self.bp += 1
        self.count +=1

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.fp == self.bp:
            return "Queue empty"
        item = self.items[self.fp]
        self.items[self.fp] = ""
        self.fp += 1
        self.count -= 1
        return item

    def peek(self):
        """Return the item at the front of the queue without removing."""
        if self.fp == self.bp:
            return "Queue empty"
        return self.items[self.fp]

    def is_empty(self):
        """Return True if the queue is empty, otherwise False."""
        return self.bp == self.fp

    def size(self):
        """Return the size (number of elements) in the queue."""
        return self.count