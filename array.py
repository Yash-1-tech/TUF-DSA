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


if __name__ == "__main__":
    arr = [-2,3,2,1,5,2,3,4,5,6,7,6,5,3,21,2,3,4,5,8]
    #print(largest_element(arr))
    #print(smallest_element(arr))
    #print(second_largest(arr))
    #print(second_smallest(arr))
    darr = sorted(arr)
    barr = sorted(arr, reverse=True)
    #print(check_sorted(arr))
    #print(check_sorted(darr))
    #print(check_sorted(barr))
    #uniqe(arr)
    #print(arr)
    #unique_set(arr)
    unique_set_write(darr)
    unique_sorted(barr)
    print(darr)
    print(barr)
