#Function alias giving a name

def greet():
    print("hello world")

hi = greet

hi()

#passing function as an argument
def greet():
    print("hello!")

def call(fun):
    fun()

call(greet)

#returing a function 
def outer():
    def inner():
        print("I'm inside")
    return inner 
robo = outer()
robo()

# A plugin system 

def add(a,b):
    return a + b
def multiply(a,b):
    return a * b
plugin = {
    "plus": add,
    "times" : multiply
}
print(plugin["plus"](2,4))
print(plugin["times"](2,78))

