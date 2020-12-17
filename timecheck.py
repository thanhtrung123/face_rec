import time

start = time.time()
while True:
    print("start: {}".format(start))
    end = time.time()
    print("end: {}".format(end))
    if end - start >= 3:
        break
print(end - start)