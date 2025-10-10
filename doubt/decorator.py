def add_sugar(func):       # decorator
    def wrapper():
        print("Adding sugar 🍬")
        func()             # call the original function
        print("Stir well ☕")
    return wrapper

@add_sugar
def make_coffee():
    print("Pouring coffee")

make_coffee()
