def next(arr):
    next_smallest = 1
    next_bigger = 1
    for i in range(len(arr)):
        if arr[i+1] > arr[i] and i >next_smallest:
            next_smallest = i+1
        if arr[next_bigger] > arr[i] > arr[0]:
            next_bigger = i
    if next_smallest != 1:
        arr[next_smallest], arr[next_smallest-1] = arr[next_smallest-1], arr[next_smallest]
    elif arr[next_bigger] > arr[0]:
        arr[next_bigger], arr[0] = arr[0], arr[next_bigger]
        return arr[0:1] + sorted(arr[1:])
    else:
        return sorted(arr)
    return arr
def reverse(arr):
    index = None
    for i in range(len(arr)-1,-1, -1):
        if arr[i] > arr[i-1]:
            index = i-1
            break
    if index == -1:
        return arr[::-1]
    for i in range(len(arr)-1,index-1, -1):
        if arr[i] > arr[index]:
            arr[i], arr[index] = arr[index], arr[i]
            return arr[:index+1] + arr[:index:-1]


arr = [
    [2,1,5,4,3,0,0],
    [3,2,1],
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    ]
for a in arr:
    print(f"loop: {reverse(a)}")


arr = [2,1,5,4,3,0,0]
print(f" no loop: {reverse(arr)}")