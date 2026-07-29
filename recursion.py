
def factorial(n):
    if n == 0 or n == 1: return 1
    return n * factorial(n-1)

def fibonacci(length,series=[0,1]):
    if length <= len(series) : return series[:length]
    series.append(series[-1]+series[-2])
    return fibonacci(length,series)

def rev_array(n, start=0, last=None):
    if last == None:
        last = len(n)-1
    if start>=last:
        return 
    temp , n[last] = n[last], n[start]
    n[start] = temp
    rev_array(n,start+1,last-1)

def index_rev(n:list):
    start = 0
    last = len(n)-1

    def swap( start:int, last:int):
        if start>=last:
            return
        n[start], n[last] = n[last], n[start]
        swap(start+1,last-1)
    return n

def mean(arr):
    n = len(arr)-1
    def worker(n):
        if n == 0:
            return arr[0]
        return arr[n] + worker(n-1)
    return worker(n)/n

def rec_palendrome(n):
    x = len(n)-1
    def worker(a, i=0):
        if i >= a//2+1:
            return True
        if n[i] != n[a]:
            return False
        else: 
            return worker(a-1,i+1)
    return worker(x)

def nor_palin(n, left = 0, right = None):
    if right == None:
        right = len(n)-1
    if left >= right:
        return True
    if n[left] != n[right]:
        return False
    return nor_palin(n ,left+1, right-1)

def nor_palint(n, left = 0):
    right = len(n)-1
    if left >= right:
        return True
    if n[left] != n[right]:
        return False
    nor_palin(n,left+1, right-1)

def palindrome(n):
    if len(n) <= 1:
        return True
    if n[0] != n[-1]:
        return False
    return palindrome(n[1:-1])

def second(n, left = 0, right = None):
    if right == None: right = len(n)-1
    if left >= right:
        return True
    if n[left] != n[right]:
        return False
    return second(n, left+1, right-1)

def count(n):
    if n <= 1:
        return 1
    print(count(n-1), end = '')
    return n

def print_count(n):
    if n <= 1 :
        print(1, end='')
    else:
        print_count(n-1)
        print(',',n, end='')

def multiple_recursion(n):
    if n <= 1:
        return n
    return multiple_recursion(n-1) + multiple_recursion(n-2) 


if __name__ == "__main__":
    #print(factorial(10))
    #print(fibonacci(10))
    #A = [1,2,3,4,5]
    #rev_array(A)
    #print(A)
    #print(index_rev(A))
    #print(mean(A))
    #print(rec_palendrome("XXXXixxXXXXX"))
    #print(second("xxxxixxxx"))
    #print(count(3))
    #print_count(10)
    #print(nor_palin("xxxxaixxxx"))
    #a = list(input("enter ").split(' '))
    #print(a[2])
    #print(multiple_recursion(8))
    i = 1
    while i <=10:
        i += 2
        print(i)
