import sys

def largest_element(arr):
    largest_element = 0
    for i in arr:
        if i > largest_element:
            largest_element = i
    return largest_element


def smallest_element(arr):
    smallest_element = arr[0]
    for i in arr:
        if i < smallest_element:
            smallest_element = i
    return smallest_element

def second_largest(arr):
    l = sl = 00
    for i in arr:
        if i > l:
            sl= l
            l = i
        elif l > i> sl:
            sl = i
    return sl

def second_smallest(arr):
    smallest = arr[0]
    runnerup = sys.maxsize
    for i in arr:
        if i < smallest:
            runnerup = smallest
            smallest = i
        elif smallest < i < runnerup:
            runnerup = i
    return runnerup

def check_sorted(arr):
    n = len(arr)
    if n <=1:
        return True
    i = 0
    j = 1
    #check for asending order
    if arr[i] > arr[j]:
        while j < n:
            if arr[i] < arr[j]:
                return False
            i+=1
            j+=1
        return True
    #check for desending order
    elif arr[i]<arr[j]:
        while j<n:
            if arr[i]>arr[j]:
                return False
            i+=1
            j+=1
        return True
    #check for duplicates
    elif arr[i] == arr[j]:
        return check_sorted(arr[1:])

def uniqe(n):
    hash_arr = [0]*100001
    i = 0
    while i<len(n):
        print(n[i],hash_arr[n[i]])
        if hash_arr[n[i]] == 1:
            del n[i]
            print(n)
        else: 
            hash_arr[n[i]] += 1
            i+=1

def unique_set(n):
    seen = set(n)
    i =0
    while i < len(n):
        if arr[i] in seen:
            seen.remove(arr[i])
            i+=1
        elif arr[i] not in seen:
            del arr[i]

def unique_set_write(n):
    uniqueset= set()
    for i in n:
        uniqueset.add(i)
    n[:] = uniqueset

def unique_sorted(n):
    i = 1
    while i < len(n):
        if n[i] == n[i-1]:
            del n[i]
        else:
            i+=1

def rotate_arr(arr,k):
    if not arr:
        return arr
    length = len(arr)
    arr[:] = arr[length-(k%length):] + arr[:length-(k%length)]

def rotate_swap(arr,k):
    if not arr:
        return arr
    length = len(arr)
    rotate = k%length
    temp = []
    temp.extend(arr[-rotate:])
    temp.extend(arr[:-rotate])
    return temp

def left_rotate(arr,k):
    if not arr:
        return arr
    rotate =k%len(arr)
    arr[:] = arr[rotate:] + arr[:rotate]

def left_swap(arr,k):
    if not arr:
        return 
    length = len(arr)
    k = k%length
    for i in range(k-1,-1,-1):
        j=i
        while j < length-(k-i):
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j+=1

def rotate_arr_optimal(arr, k):
    n = len(arr)
    if n == 0: return arr
    k = k % n
    def reverse(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

def zero_end(arr):
    n = 0
    temp = []
    for i in arr:
        if i != 0:
            temp.append(i)
        else:
            n+=1
    zero = [0] * n
    arr[:] = temp + zero

def while_zero(arr):
    i = 0
    count = 0
    n = len(arr)
    while i<n and arr[i]!=0:
        count+=1
        i+=1
    j = i+1
    while j<n:
        if arr[j] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1
        j+=1
        count+=1  
    print(count)

def move_zeroes(arr):
    i = 0
    count = 0
    for j in range(len(arr)):
        count +=1
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    print(count)

def union_sorted(arr1,arr2):
    union =[]
    i = j = 0
    n =len(arr1)
    m = len(arr2)
    while i<n or j<m:
        while i<n-1:
            if arr1[i] == arr1[i+1]:
                i+=1
            else: break
        while j<m-1:
            if arr2[j]==arr2[j+1]:
                j+=1
            else: break
        if i == n:
            union.append(arr2[j])
            j+=1
        elif j == m:
            union.append(arr1[i])
            i+=1
        elif arr1[i] == arr2[j]:
            union.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i] < arr2[j]:
            union.append(arr1[i])
            i+=1
        else:
            union.append(arr2[j])
            j+=1
    return union

def intersectin(arr1, arr2):
    n ,m = len(arr1), len(arr2)
    i, j = 0,0
    intersection = []
    while i < n and j < m:
        while i < n-1:
            if arr1[i] == arr1[i+1]:
                i+=1
            else:
                break
        while j < m-1:
            if arr2[j] == arr2[j+1]:
                j+=1
            else:
                break
        if arr1[i]==arr2[j]:
            intersection.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i] > arr2[j]:
            j+=1
        else:
            i+=1
    return intersection
    
if __name__ == "__main__":
    #arr = [-2,3,2,1,5,2,3,4,5,6,7,6,5,3,21,2,3,4,5,8]
    #print(largest_element(arr))
    #print(smallest_element(arr))
    #print(second_largest(arr))
    #print(second_smallest(arr))
    #n =[1,2]
    #darr = sorted(arr)
    #barr = sorted(arr, reverse=True)
    #print(check_sorted(arr))
    #print(check_sorted(darr))
    #print(check_sorted(barr))
    #uniqe(arr)
    #print(arr)
    #unique_set(arr)
    #unique_set_write(darr)
    #unique_sorted(barr)
    #print(darr)
    #print(barr)
    #print(rotate_arr(arr,50))
    #rotate_swap(arr,46)
    #left_swap(arr,2)
    #rotate_arr(arr,46)
    #left_rotate(n,47)
    #print(n)
    #x = [0,100,101,0,0,2,20,0,0,2,0,4,5,0,6]
    #y = [1,2,3,4,5,66,7,8,9,0,0,0,0,0,0,1,2,3,4,5,6,7,8,0,4,5,0]
    #zero_end(x)
    #while_zero(x)
    #move_zeroes(y)
    #print(x)
    '''
    arr1 = [1,1,2,3,4,4]
    arr2 = [2,3,4,4,5,5]
    '''
    arr1 = [0,1,3,4,4,4,5,6,7,8,9,10]
    arr2 = [0,5,5,6,6,6]
    print(union_sorted(arr1, arr2))
