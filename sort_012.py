def sort_012(arr):
    length = len(arr)
    low = 0
    high = length-1
    while high >= 0 and arr[high] == 2:
        high-=1
    for i in range(length):
        if arr[i] == 2:
            if i >= high:
                break
            elif arr[high] != 2:
                arr[i], arr[high] = arr[high], arr[i]
            else:
                arr[i], arr[high-1] = arr[high-1], arr[i]
                high-=1
        if arr[i] == 0:
            if i <= low:
                continue
            elif arr[low] !=0:
                arr[i], arr[low] = arr[low], arr[i]
            else:
                arr[i], arr[low+1] = arr[low+1], arr[i]
                low+=1

def dutch_flagman(arr):
    low = mid = 0
    high = len(arr)-1
    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low+=1
            mid+=1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high-=1
        else:
            mid+=1
        
if __name__ == "__main__":
    arr = [
    [2,1,0],
    [2,2,1,1,0,0],
    [0,2,1],
    [2,0,1],
    [1,2,0],
    [2,1,2,1,0,0,1,2],
    [2,0,2,1,1,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    ]
    for a in arr:
        dutch_flagman(a)
        print(a)

    arr = [0, 2, 1, 0, 2, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 2, 0, 2, 0, 0, 1, 2, 0, 2, 1, 1, 2, 1, 1, 0, 1, 1]
    sort_012(arr)
    print(arr)