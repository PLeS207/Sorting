import random
import matplotlib.pyplot as plt


def find_smallest(lst):
    s = lst[0]
    s_index = 0
    for i in range(1, len(lst)):
        if lst[i] < s:
            s = lst[i]
            s_index = i
    return s_index


def sorting(lst):
    new_lst = []
    N = len(lst)
    for i in range(N):
        smallest = find_smallest(lst)
        new_lst.append(lst.pop(smallest))
    return new_lst


plt.plot(sorting([random.randint(1, 3000) for i in range(1000)]))
plt.ylabel('Sorted numbers')
plt.show()
