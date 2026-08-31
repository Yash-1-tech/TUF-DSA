arr = [1,3,5,7]
arr2 = [0,2,6,8,9]

def work(arr,arr2):
    i = (len(arr) - 1)
    j = 0
    while i >=0 and j <len(arr2) and  arr[i]> arr2[j]:
        arr[i], arr2[j] = arr2[j], arr[i]
        i-=1
        j+=1
    return sorted(arr), sorted(arr2)


def merger_shell(arr1, arr):
    n = len(arr1)
    m = len(arr2)
    total_len = n+m
    from math import ceil as ceil
    gap = ceil(total_len/2)
    while gap > 0:
        i = 0
        j = gap

        while j < total_len:
            if i < n and j < n:
               if arr1[i] > arr1[j]:
                   arr1[i], arr1[j] = arr1[j], arr1[i]

            elif i < n and j >= n:
               j_ind = j - n
               if arr1[i] > arr2[j_ind]:
                   arr1[i], arr2[j_ind] = arr2[j_ind], arr1[i]\
            
            elif i >= n and j >=n:
                i_ind = i - n
                j_ind = j - n
                if arr2[i_ind] > arr2[j_ind]:
                    arr2[i_ind], arr2[j_ind] = arr2[j_ind], arr[i_ind]

            i +=1
            j +=1

        if gap == 1:
           break
        gap = ceil(gap/2)

def repeated_missing(arr):
    current = xor = repeat = 0
    length = len(arr)
    seen = [0] * (length+1)
    for i in range(length):
        xor ^= i+1
        if seen[arr[i]] == 0:
            seen[arr[i]] = 1
            current ^= arr[i]
            
        else:
            repeat = arr[i]
            seen[arr[i]] +=1
    return xor^current, repeat

def summation(arr):
    xor =  0
    x = 0 
    y = 0
    n = len(arr)

    for i in range(1,n+1):
        xor ^= i

    for i in range(n):
        xor ^= arr[i]

    bit = xor & -xor

    for i in range(1,n+1):
        if i & bit:
            x ^= i
        else: y^=i

    for num in arr:
        if num & bit:
            x^=num
        else: y ^= num

    if x in arr:
        repeated = x
        missing = y
    else:
        repeated = y
        missing = x

    return repeated, missing




print(summation([4,3,6,2,1,1]))
"""merger_shell(arr,arr2)
print(arr,arr2)"""