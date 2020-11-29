import random
import matplotlib.pyplot as plt
import time


def stend(f, *args):
    t1 = time.perf_counter()
    f(*args)
    t2 = time.perf_counter()
    delta = t2 - t1
    return delta


N = 40000
avg_time = []
for i in range(N):
    avg_time.append(stend(sorted, [random.randint(1, 3000) for i in range(i)]))
    print(i)

plt.ylabel('Time')
plt.xlabel('Count Element')

plt.plot(avg_time)

plt.show()
