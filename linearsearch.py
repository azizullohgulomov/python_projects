def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

arr = [5, 3, 8, 4, 2]
target = 8
index = linear_search(arr, target)
if index != -1:
    print(f"{target} found at index {index}.")
else:
    print(f"{target} not found in the list.")