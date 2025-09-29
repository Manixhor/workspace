import threading
import time 

def walk_dog():
    time.sleep(8) #the time taken to take the dog walk
    print("taking walk ")

def take_mail():
    time.sleep(2)
    print("mail taken from the box")

def take_out_trash():
    time.sleep(4)
    print("trash taken out")

walk_dog()
take_mail()
take_out_trash()
