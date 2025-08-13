import threading
import time

def wash_dishes():
    print("Started washing dishes...")
    time.sleep(3)  # Pretend it takes 3 seconds
    print("Finished washing dishes!")

# Create a thread for washing dishes
dish_thread = threading.Thread(target=wash_dishes)

# Start the thread
dish_thread.start()

print("Meanwhile, I'm baking a cake!")
