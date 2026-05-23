def findsum(arr, target):
    res = []
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i], arr[j]) in res or (arr[j], arr[i]) in res:
                continue

            if arr[i] + arr[j] == target:
                res.append((arr[i], arr[j]))
                
    return [list(pair) for pair in res]         


arr=[1, 1, 2, 3]
target=4

print(findsum(arr, target))
print(findsum([3,3,3], 6))
print(findsum([1,1,2,3], 4))
print(findsum([1,2,3], 10))