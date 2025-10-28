import threading
import time 


def walk():
    time.sleep(9)
    print("dog is walking")

def take_out():
    time.sleep(2)
    print("take out trash")

def mail():
    time.sleep(4)
    print("got the mail ")
walk()
take_out()
mail()