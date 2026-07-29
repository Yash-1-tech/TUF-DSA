arr = [1,2,3,2,1,4]

hash_arr = [0]* 10001
map = {}
for i in arr:
    map[i] = map.get(i, 0) + 1
    print(f"  {i} -> {map[i]}")
    hash_arr[i] += 1

#print(f'frequency of 1 is {hash_arr[1]}')
#print(f'frequency of 4 is {hash_arr[4]}')
#print(hash(hash('apple')))

def max_min_hz(arr):
    max_item = []
    min_item = []
    max_count = float('-inf')  # Start at lowest possible value
    min_count = float('inf')   # Start at highest possible value
    # Bug Fix 1: Use .items() to loop through a dictionary
    for i,j in arr.items():
        if j > max_count:
            max_count = j
            max_item = [i]

        elif j == max_count:
                max_item.append(i)

        if min_count == None:
            min_count = j

        if j < min_count:
            min_item = [i]
            min_count = j

        elif j == min_count:
            min_item.append(i)

    return f"max fquency is {max_count} of {max_item} and min frequency is {min_count} of {min_item}"

print(max_min_hz(map))