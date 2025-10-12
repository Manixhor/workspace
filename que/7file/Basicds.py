class DS:
    def __init__(self):
        # Create an empty list
        self.items = []
        
    # Stack methods
    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} to stack")
    
    def pop(self):
        if not self.items:
            print("Stack is empty")
            return None
        item = self.items.pop()
        print(f"Popped {item} from stack")
        return item
    
    # Queue methods
    def enqueue(self, item):
        self.items.append(item)
        print(f"Added {item} to queue")
    
    def dequeue(self):
        if not self.items:
            print("Queue is empty")
            return None
        item = self.items.pop(0)
        print(f"Removed {item} from queue")
        return item

    # Peek method
    def peek(self):
        if not self.items:
            print("Nothing to peek at")
            return None
        print(f"Peek: {self.items[-1]}")
        return self.items[-1]

# Let's test it!
toy_box = DS()

toy_box.push("Car")
toy_box.push("Doll")
toy_box.peek()        # See what’s on top
toy_box.pop()         # Take the top toy out

# Queue play 🚂
toy_box.enqueue("Ball")
toy_box.enqueue("Teddy")
toy_box.dequeue()     # First toy out of line
