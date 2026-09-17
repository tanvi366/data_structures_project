from dsa.data_structures.linked_list import LinkedList, Node

def test_empty_linked_list():
    l = LinkedList()
    assert l.head is None
    assert l.length() == 0

def test_node_creation():
    node = Node(10)
    assert node.value == 10
    assert node.next is None

def test_add_one_node():
    linked_list = LinkedList()
    linked_list.add(1)
    assert linked_list.head.value == 1
    assert linked_list.head.next is None
    assert linked_list.length() == 1

def test_add_multiple_nodes():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)

    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 3
    assert linked_list.length() == 3

def test_add_preserves_order():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 3

def test_prepend_to_empty_list():
    linked_list = LinkedList()
    linked_list.prepend(1)
    assert linked_list.head.value == 1
    assert linked_list.head.next is None
    assert linked_list.length() == 1

def test_prepend_to_existing_list():
    linked_list = LinkedList()
    linked_list.add(2)
    linked_list.add(3)
    linked_list.prepend(1)
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 3
    assert linked_list.length() == 3

def test_search_existing_value():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    assert linked_list.search(2) is True

def test_search_missing_value():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    assert linked_list.search(4) is False

def test_search_empty_list():
    linked_list = LinkedList()
    assert linked_list.search(2) is False

def test_length_empty_list():
    linked_list = LinkedList()
    assert linked_list.length() == 0

def test_length_multiple_nodes():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    assert linked_list.length() == 3

def test_insert_after_existing_node():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(4)
    linked_list.insert(2,3)
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 3
    assert linked_list.head.next.next.next.value == 4
    assert linked_list.length() == 4

def test_insert_at_position_zero():
    linked_list = LinkedList()
    linked_list.add(2)
    linked_list.add(3)
    linked_list.insert_at_position(0,1)
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 3

def test_insert_at_position_middle():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(3)
    linked_list.add(4)
    linked_list.insert_at_position(1,2)
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 3
    assert linked_list.head.next.next.next.value == 4

def test_insert_at_position_end():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.insert_at_position(3,4)
    assert linked_list.head.next.next.next.value == 4
    assert linked_list.length() == 4

def test_revenge_empty_list():
    linked_list = LinkedList()
    linked_list.reverse()
    assert linked_list.head is None
    assert linked_list.length() == 0

def test_reverse_one_node():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.reverse()
    assert linked_list.head.value == 1
    assert linked_list.head.next is None

def test_reverse_multiple_nodes():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.reverse()
    assert linked_list.head.value == 3
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 1
    assert linked_list.head.next.next.next is None

def test_delete_head():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.delete(1)
    assert linked_list.head.value == 2
    assert linked_list.head.next.value == 3
    assert linked_list.length() == 2

def test_delete_middle():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.delete(2)
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 3
    assert linked_list.length() == 2

def test_delete_tail():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.delete(3)
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 2
    assert linked_list.length() == 2

def test_delete_only_node():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.delete(1)
    assert linked_list.head is None
    assert linked_list.length() == 0

def test_delete_missing_value():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    assert linked_list.delete(4) == "Input Error"
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 3
    assert linked_list.length() == 3
