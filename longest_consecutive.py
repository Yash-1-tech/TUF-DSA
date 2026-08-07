def longest_consecutive(arr):
    got = sorted(arr)
    longest = count = 1
    
    for i in range(len(got)-1):
        if got[i] + 1 == got[i+1]:
            count+=1
        elif count > longest:
                longest = count
                count = 1
        else:
            count = 1
    return longest

def longest_consecutive_set(arr):
    got = set(arr)
    longest = 1
    for i in got:
        if i-1 not in got:
            count = 1
            upper_bound = i+1
            while upper_bound in got :
                upper_bound+=1
                count+=1
        longest = max(longest, count)
    return longest
              

print(longest_consecutive_set([102,4,100,1,101,3,2,1,1]))
