# Reverse the Order of Elements in a Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")

    def __str__(self):
        return str(self.items)


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def __str__(self):
        return str(self.items)


def reverse_queue(queue):
    stack = Stack()
    
    # Dequeue all items from the queue and push them onto the stack
    while not queue.is_empty():
        stack.push(queue.dequeue())
    
    # Pop all items from the stack and enqueue them back to the queue
    while not stack.is_empty():
        queue.enqueue(stack.pop())


# Demonstration
if __name__ == "__main__":
    q = Queue()
    for i in range(1, 6):
        q.enqueue(i)
    
    print("Queue before reversal:", q)
    reverse_queue(q)
    print("Queue after reversal:", q)