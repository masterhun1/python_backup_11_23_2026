import time 
# 1. Get the current Unix timestamp
epoch_seconds = time.time()
print(f"Seconds since epoch: {epoch_seconds}")
# 2. Pause program execution for 1.5 seconds
print("Waiting...")
time.sleep(1.5)
print("Done waiting!")
