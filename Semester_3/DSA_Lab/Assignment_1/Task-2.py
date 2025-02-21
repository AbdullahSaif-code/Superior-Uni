# Implementing a Queue using Python

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self):
        user = int(input("How many values u want to add: "))
        for i in range(user):
            item = input("Enter the value: ")
            self.queue.append(item)
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            self.queue.pop(0)
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.queue)
    def front(self):
        return self.queue[0]
Queue = Queue()
Queue.enqueue()   # Run enqueue method to add values in Queue
Queue.dequeue()    # Run dequeue method to remove values from Queue
print(Queue.is_empty())  # Check if Queue is empty or not
print(Queue.size())       # Check the size of Queue
print(Queue.front())      # Check the front value of Queue