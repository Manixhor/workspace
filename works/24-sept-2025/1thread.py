import time
import threading

def do_homework():
    print("Starting homework...")
    time.sleep(3)
    print("Finished homework!")

def fold_clothes():
    print("Starting to fold clothes...")
    time.sleep(3)
    print("Finished folding clothes!")

# Create threads
homework_thread = threading.Thread(target=do_homework)
clothes_thread = threading.Thread(target=fold_clothes)

homework_thread.start()
clothes_thread.start()

# Wait for both to finish
homework_thread.join()
clothes_thread.join()

print("Both tasks are done!")
