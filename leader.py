def leader(arr):
    list = [arr[-1]]
    max = arr[-1]
    length = len(arr)
    for i in range(length-2,-1,-1):
        if arr[i] > max:
            max = arr[i]
            list.append(arr[i])
    return list[::-1]

arr = [10,22,12,3,0,6]
print(leader(arr))
