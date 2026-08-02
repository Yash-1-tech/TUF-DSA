def dict_2sum(arr,n):
    hash_arr = [0]*(n+1)
    for i in arr:
        if i>n:
            continue
        if hash_arr[i] == 0:
            hash_arr[n-i]  = i
        else:
            return True , hash_arr[i], i
    return False

def dict_2sum(arr,n):
    dict = {}
    for i in arr:
        if i not in dict:
            dict[n-i] = i
        else:
            return True, dict[i] , i
    return False

def dict_2sum_index(arr,n):
    seen ={}
    for index, num in enumerate(arr):
        if n - num in seen:
            return [seen[n-num], index]
        seen[num] = index
    return []

if __name__ == "__main__":
    print(dict_2sum([5, 4, 2, 5, 2],7))
    print(dict_2sum([5, 4, 2, 5, 2],7))
