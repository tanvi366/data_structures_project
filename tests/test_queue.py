from dsa.data_structures.queues import Queue

def test_queue():
    queue = Queue()
    assert queue.is_empty()
    assert queue.size() == 0
    assert queue.peek() == "Queue empty"
    assert queue.dequeue() == "Queue empty"

def test_one_element():
    queue = Queue()
    queue.enqueue(1)
    assert queue.size() == 1
    assert queue.peek() == 1

def test_multiple_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1
    assert queue.size() == 3

def test_fifo_order():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 1
    assert queue.dequeue() == 1
    assert queue.peek() == 2

def test_size_decrease_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 1
    assert queue.size() == 2
    assert queue.dequeue() == 1
    assert queue.size() == 1

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.dequeue() == 1
    assert queue.size() == 0
    assert queue.peek() == "Queue empty"
    assert queue.dequeue() == "Queue empty"

def test_peek_does_not_remove():
    queue = Queue()
    queue.enqueue(1)
    assert queue.peek() == 1
    assert queue.peek() == 1
    assert queue.size() == 1
    assert queue.dequeue() == 1

def test_max_capacity():
    queue = Queue()
    for i in range(5):
        queue.enqueue(i)
    assert queue.size() == 5

def test_enqueue_when_full():
    queue = Queue()
    for i in range(5):
        queue.enqueue(i)
    assert queue.enqueue(6) == "Queue Full"
    assert queue.size() == 5
    assert queue.dequeue() == 0

def test_dequeue_all_items():
    queue = Queue()
    for i in range(5):
        queue.enqueue(i)
    assert queue.size() == 5
    for i in range(5):
        queue.dequeue()
    assert queue.size() == 0

def test_max_FIFO():
    queue = Queue()
    for i in range(5):
        queue.enqueue(i)
    assert queue.size() == 5
    for i in range(5):
        assert queue.dequeue() == i
    assert queue.size() == 0

def test_bp_fp_one_element():
    queue = Queue()
    queue.enqueue(1)
    assert queue.fp == 0
    assert queue.bp == 1

def test_bp_fp_two_element():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.fp == 0
    assert queue.bp == 2

def test_bp_fp_enqueue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    assert queue.fp == 1
    assert queue.bp == 2

def test_full_queue_dequeue_then_enqueue():
    queue = Queue()
    for i in range(5):
        queue.enqueue(i)
    assert queue.dequeue() == 0
    assert queue.enqueue(1) == "Queue Full"