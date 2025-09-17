
# def hello(name):
#     return f"hello world,{name}"

# name = input("enter your name \n")
# print(hello(name))

#example for args 

def add(*args):
    return sum(args)

print(add(2,3,4,5))
#it will add n no of values 


def info(**kwargs):
    return kwargs
print(info(name = "mani",age=20))
#it prints as dict 