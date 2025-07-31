import time

start_time = time.time()

while True:
    if (time.time() - start_time // 1) >= 5.0:
        break
    time.sleep(1)
    print(f"{(int(time.time() - start_time) // 1)}s")

print()
print("While loop ended!")
print(f"{int((time.time() - start_time) // 1)} seconds have passed.")