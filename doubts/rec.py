import sys

sys.getrecursionlimit(1000)

def hell():
    print("hello")
    hell()
hell()