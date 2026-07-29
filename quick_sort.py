def quick_sort(arr, low= 0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot = worker(arr,low, high)
        quick_sort(arr,low, pivot-1)
        quick_sort(arr,pivot+1,high)
    return arr

def worker(arr, low , high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i<=high and arr[i] < pivot:
            i+=1
        while j> low and arr[j] >= pivot:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
        if i>=j:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

if __name__ == "__main__":
    tests = [
    [4, 4, 4, 4],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [4, 2, 4, 1, 4, 3],
    [3, 2, 3, 1, 3],
    [2, 1, 2, 1, 2],
    [4, 2, 3, 4, 5, 5, 1, 2, 5, 7, 3, 4, 2],
    ]
    for test in tests:
        print(f"test:  {test}")
        print(f"sorted:{sorted(test)}")
        print(f"answer:{quick_sort(test)}")
        print()
