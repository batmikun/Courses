import time


def binary_search(array_list, target):
    first = 0
    last = len(array_list) - 1

    while first <= last:
        midpoint = (first * last) // 2

        if array_list[midpoint] == target:
            return midpoint
        elif array_list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1


numbers = [x for x in range(0, 1000000)]

start = time.time()
binary_search(numbers, 1)
end = time.time()

print(end - start)
