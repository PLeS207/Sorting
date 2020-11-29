import random
import matplotlib.pyplot as plt


def q(a):
    if len(a) < 2:
        return a
    else:
        mid = a[0]
        less = []
        more = []
        for i in a[1:]:
            if i > mid:
                more.append(i)
            else:
                less.append(i)
    return q(less) + [mid] + q(more)


plt.plot(q([random.randint(1, 3000) for i in range(1000)]))
plt.ylabel('Sorted numbers')
plt.show()
