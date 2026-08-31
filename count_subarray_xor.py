def count(arr,k):
    data = []
    count = 0
    on = 0
    for i in range(len(arr)):
        current = arr[i]^0 
        if current == k:
            count +=1 
        if k - current in data:
            count +=1
        on = on ^ current
        data.append(on)
    return count,data

print(count([4,2,2,2,2,6,4,2,2],6))