def majority(arr):
    hash_map ={}
    for i in arr:
        hash_map[i] = hash_map.get(i,0) + 1
        if hash_map[i] >= len(arr)/2:
            return i

def moores_voting(arr):
    candidate = None
    margine = 0
    for i in arr:
        if i == candidate:
            margine +=1
        else:
            margine -=1
        if margine <0:
            candidate = i
            margine = 1
    return candidate

arr = [7,7,5,7,5,1,5,6,5,7,7,5,5,5]
print(majority(arr))
print(moores_voting(arr))