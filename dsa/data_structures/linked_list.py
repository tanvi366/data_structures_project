class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """Represent a linked list of nodes connected by references."""
    def __init__(self):
        self.head = None

    def add(self,data):
        """Add an item to the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    
    def insert(self,prev, new_value):
        """Insert item after a specific item in the list."""
        new_node = Node(new_value)

        current = self.head
        while current:
            if current.value == prev:
                break
            current = current.next
        if current.value != prev:
            return "Input Error"
        new_node.next = current.next
        current.next = new_node

    def prepend(self, value):
        """Add an item to the beginning of the linked list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def search(self, value):
        """Return True if the item is found in the linked list, otherwise false."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def length(self):
        """Return length of linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def insert_at_position(self, index, value):
        """Insert item at entered index in the linked list."""
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        count = 0
        current = self.head
        while current and count < index - 1:
            count+=1
            current = current.next
        new_node.next = current.next
        current.next = new_node

    #  10 -> 12 -> 24

    def reverse(self):
        """Reverse the order of the items in the linked list."""
        current = self.head
        previous = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous


    def delete(self, value):
        """Remove the first occurence of an item in the list and return True if found."""
        current=self.head
        previous=None
        while current:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return "Input Error"

    def display(self):
        """Display all items in the linked list."""
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")