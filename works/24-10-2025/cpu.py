import psutil 
import time 

print("checking CPU usage")

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"{cpu_usage}")
    time.sleep(1)