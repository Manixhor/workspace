
def info(**kwargs):
    return kwargs

print(info(Name="Mani",age= 10))


def add(*args):
    return sum(args)

print(add(3,4))

add = lambda  x,y : x +y
print(add(3,5))


for i in range(1,5):
    if i == 2:
        break 
    print(i)