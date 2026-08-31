def overlap(arr):
    arr.sort()
    collection = [arr[0]]
    for i,j in arr[1:]:
        low, high = collection[-1]
        if i <= high:
            collection[-1] = (low,max(j,high))
        else:
            collection.append((low,high))
    return collection

arr = [(1,3),(2,6),(8,9),(9,11),(8,10),(2,4),(15,18), (16,17)]
print(overlap(arr))