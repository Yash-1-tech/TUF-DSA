def longest_subarray(arr,k):
    current = longest = []
    current_sum = 0
    for i in arr:
        if i > k:
            current = []
            current_sum = 0
        if i < k:
            if current_sum + i > k:
                current.append(i)
                current_sum += i
                while current_sum > k:
                    del current[0]
                    current_sum -= current[0]
            elif current_sum + i == k:
                if len(longest) < len(current) + 1:
                    longest = current.copy() 
                    longest.append(i)
                current = []
                current_sum = 0
            else:
                current_sum += i
                current.append(i)
        if i == k:
            current = [i]
            if len(longest) < len(current):
                longest = current.copy()
                longest.append(i)
            current = []
            current_sum = 0
    return longest

def sliding_window_2ptrs(arr, k):
    current_sum = 0
    start = last = longest = None
    for i in range(len(arr)):
        current_sum+=arr[i]
        if start is None: start = i
        while current_sum > k:
            current_sum -= arr[start]
            start+=1
        if current_sum == k:
            last = i
            if longest is None: 
                longest = [start, last]
            elif (last - start) > (longest[1] - longest[0]):
                longest = [start, last]
            current_sum-=arr[start]
            start +=1
            last = None
    if longest: return arr[longest[0]:longest[1]+1]

if __name__ == "__main__":
    #arr = [1,1,2,1,1,3,1,1,1,4,2,3]
    b = [8, 8, 2, 6, 5, 5, 5, 4, 6, 1, 3, 2]
    a = [7, 7, 7, 7, 3, 2, 3, 4, 5, 7, 2, 1]
    print(sliding_window_2ptrs(a,24))
    print(sliding_window_2ptrs(b,11))
