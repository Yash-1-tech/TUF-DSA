def maximum_subarray(arr):
    i = start = 0
    length = len(arr)
    max = sum(arr)
    j = last = length-1
    while i<=j:
        temp =sum(arr[i:j+1])
        if temp > max:
            max = temp
            start = i
            last = j +1
        elif arr[i] > arr[j]:
            j-=1
        else: 
            i+=1
    return max, arr[start:last]

arr = [-2,-3,4,-1,-2,1,5,-3]

def max_sum_subarray(arr):
    maximum = sum = 0
    for i in arr:
        sum += i
        if sum > maximum:
            maximum = sum

        if sum < 0:
            sum = 0
    return maximum

ans, array = maximum_subarray(arr)
print(ans, array)
print(max_sum_subarray(arr))

i = -2
sum = 0
sum+=i
print(sum)