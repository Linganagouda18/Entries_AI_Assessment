#Second largest in array
def largest(arr):
    arr.sort()

    n = len(arr)
    return arr[n-2]


arr = [3, 1, 4, 1, 5, 9, 2, 6]
# arr = [10, 10, 10]
# arr = [5, 3]
# arr = [-1, -2, -3]
res = largest(arr)
print(res)

