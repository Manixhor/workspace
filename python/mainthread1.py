import threading
import time 


def walk(first):
    time.sleep(9)
    print(f"{first} is walking")

def take_out():
    time.sleep(2)
    print("take out trash")

def mail():
    time.sleep(4)
    print("got the mail ")

thread1 = threading.Thread(target=walk,args = ("random",))
thread1.start()
thread2 = threading.Thread(target=take_out)
thread2.start()
thread3 = threading.Thread(target=mail)
thread3.start()

thread1.join()
thread2.join()
thread3.join()
print("all are done !")