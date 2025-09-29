import threading
import time 

def walk_dog(name):
    time.sleep(8) #the time taken to take the dog walk
    print(f"taking walk {name} ")

def take_mail():
    time.sleep(2)
    print("mail taken from the box")

def take_out_trash():
    time.sleep(4)
    print("trash taken out")

chore1 = threading.Thread(target=walk_dog,args = ("chintu",))
chore1.start()

chore2 = threading.Thread(target=take_mail)
chore2.start()

chore3 = threading.Thread(target=take_out_trash)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("all are done ")