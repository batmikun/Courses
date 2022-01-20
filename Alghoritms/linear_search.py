import time

def linear_search(array_list, target):
    """
    Return the index position of the target if found, else returns None
    """

    for i in range(0, len(array_list)):
        if array_list[i] == target:
            return i

    return None


def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")


numbers = [x for x in range(0, 1000000)]

start = time.time()
result = linear_search(numbers, 1000000)
verify(result)
end = time.time()
print(end - start)
