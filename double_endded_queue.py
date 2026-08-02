from collections import deque

def rotate_deque(arr,k):
    d = deque(arr)
    d.rotate(k%(len(arr)-1))
    return list(d)

print(rotate_deque([1,2,3,4,5,6,7],3))
