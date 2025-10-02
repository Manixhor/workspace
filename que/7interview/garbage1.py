class Demo:
    def __init__(self, name):
        self.name = name
        print(f"Object '{self.name}' is CREATED ✅")

    def __del__(self):
        print(f"Object '{self.name}' is DESTROYED ❌ (Garbage Collected)")
        

# Create an object
obj1 = Demo("A")

# Make another reference to the same object
obj2 = obj1

# Remove one reference
del obj1
print("Deleted obj1, but obj2 still exists!")

# Remove last reference
del obj2
print("Deleted obj2 — no references left now!")
