import time

numbers = [x for x in range(0, 1000000)]


def recursive(array_list, target):
    if len(array_list) == 0:
        return False

    midpoint = (len(array_list)) // 2

    if array_list[midpoint] == target:
        return True

    if array_list[midpoint] < target:
        return recursive(array_list[midpoint + 1:], target)

    return recursive(array_list[:midpoint], target)


def verify(i):
    print("Target Found: ", i)


start = time.time()
result = recursive(numbers, target=1)
end = time.time()
verify(result)
print(end - start)
