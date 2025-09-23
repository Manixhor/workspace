import threading
import time

def background_task():
    while True:
        print("Background task running...")
        time.sleep(1)

# Create daemon thread
t = threading.Thread(target=background_task)
t.daemon = True
t.start()

# Main thread sleeps briefly
time.sleep(3)
print("Main thread exiting...")
