from collections import deque
def rearange(arr):
    i = 0
    n = deque()
    j = deque()
    while i < len(arr):
        if i % 2 == 0 and arr[i] < 0:
           n.append(i)
        elif i%2 != 0 and arr[i]>0:
            j.append(i)
        if n and j:
            arr[n.popleft()], arr[j.popleft()] = arr[j[0]], arr[n[0]]
        i+=1

def swap_arrange(arr):
    positive = 0
    negative = 1
    length = len(arr)
    while positive < length and negative < length:
        while positive < length and arr[positive] > 0:
            positive+=2
        while negative < length and arr[negative] < 0:
            negative+=2
        if positive < length and negative < length:
            arr[positive], arr[negative] = arr[negative], arr[positive]
            positive+=2
            negative+=2

arr = [3,1,-2,-2,5,-4,-5,-5,-5,1,1,1,1,1,-6,-6,1]
#rearange(arr)
swap_arrange(arr)
print(arr)

