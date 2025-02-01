# Simulate a Ticketing System Using a Queue
class TicketingSystem:
    def __init__(self):
        self.queue = []

    def enqueue(self, customer):
        self.queue.append(customer)
        print(f"Customer {customer} has joined the queue.")

    def dequeue(self):
        if self.queue:
            served_customer = self.queue.pop(0)
            print(f"Customer {served_customer} has been served.")
        else:
            print("No customers in the queue.")

    def display_queue(self):
        if self.queue:
            print("Current queue:", self.queue)
        else:
            print("The queue is empty.")

# Example usage
ticketing_system = TicketingSystem()
ticketing_system.enqueue("Ali")
ticketing_system.enqueue("Hamza")
ticketing_system.enqueue("Hader")
ticketing_system.display_queue()
ticketing_system.dequeue()
ticketing_system.display_queue()
ticketing_system.dequeue()
ticketing_system.dequeue()
ticketing_system.dequeue()