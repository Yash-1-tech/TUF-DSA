def quick(n, low = 0, high = None):
    if high is None:
        high = len(n)-1
    if low < high:
        pivot = worker(n,low,high)
        quick(n, low ,pivot-1)
        quick(n, pivot+1, high)
    return n
    

def worker(n, low, high):
    pivot = n[low]
    i = low+1
    j = high
    while True:
        while i<= high and n[i]<= pivot:
            i+=1
        while j >= low and n[j]>pivot:
            j-=1
        if i < j:
            n[i], n[j] = n[j], n[i]
        if i >= j:
            break
    n[low], n[j] = n [j], n[low]
    return j


arr = [4, 2, 3, 4, 5, 5, 1, 2, 5, 7, 3, 4, 2]

tests = [
    [4, 4, 4, 4],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [4, 2, 4, 1, 4, 3],
    [3, 2, 3, 1, 3],
    [2, 1, 2, 1, 2],
]
for i in tests:
    print(quick(i))


