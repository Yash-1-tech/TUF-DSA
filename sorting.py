def selection(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i,n):
            if arr[j] < arr[i]:
                min_index = j
        arr[i] ,arr[min_index] = arr[min_index], arr[i]

def bubble(arr):
    length = len(arr)
    for _ in range(length):
        swap = False
        for i in range(length-1):
            if arr[i] > arr[i+1]:
                arr[i] ,arr[i+1] = arr[i+1], arr[i]
                swap = True
        if not swap:
            break

def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j]> key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 

def shell(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i 
            while j>=gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    
def merge_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    mid = length//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    arr = [4,3,2,5,6,8,7,4,5,7,1]
    print(merge_sort(arr))
    #selection(arr)
    #bubble(arr)
    #insertion(arr)
    #shell(arr)
    #print(arr)