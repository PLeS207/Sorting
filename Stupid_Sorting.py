import random
import matplotlib.pyplot as plt


def sorting(a):
    changed = True
    while changed:
        for i in range(len(a) - 1):
            for i in range(len(a) - 1):
                changed = False
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    changed = True
    return a


plt.plot(sorting([random.randint(1, 3000) for i in range(1000)]))
plt.ylabel('Sorted numbers')
plt.show()
