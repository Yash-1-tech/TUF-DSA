arr = [5,3,2,4,1]
count = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            count+=1

print(count)

count = 0 
seen = [arr[0]]
for i in range(1,len(arr)):
    if arr[i] < seen[-1]:
        count += 1