import math as m

def countnrev(n):
    rev = 0
    count = 0
    while n>0:
        temp = n%10
        n = n//10 
        rev = rev*10 + temp
        count += 1
    return rev, count

def palendrome(n):
    rev = 0
    while n>rev:
        rev = rev*10 +(n%10)
        n = n//10
    return rev == n or n == rev//10

def Opalendrome(n):
    x = len(n)-1
    for i in range(x//2+1):
        if n[i] != n[x-i]:
            return False
    return True
        
def armstrongno(n):
    or_n = n
    summ = 0
    power = m.ceil(m.log10(n))
    while n>0:
        summ =  summ + ((n%10) ** power)
        n = n//10
    return summ == or_n

def alldivisor(n):
    A = [1,n]
    count =0
    for i in range(2,n):
        if n%i == 0: A.append(i)
        count += 1
    return A, count

def method(n):
    A=[1,n]
    exclude = []
    count = 0

    for i in range(2,n):
        if any(i % x == 0 for x in exclude):
            continue
        if n%i == 0: A.append(i)
        else: exclude.append(i)
        count += 1
    return A, count

def dualdivisor(n):
    A=[1]
    rev =[]
    for i in range(2,m.floor(m.sqrt(n))):
        if n%i == 0:
            A.append(i)
            rev.append(n//i)
    rev.reverse()
    A = A + rev
    A.append(n)
    return A

def divisor(n):
    A=[1]
    rev =[]
    i = 2
    while i*i<=n:
        if n%i == 0:
            A.append(i)
            if i * i != n:
                rev.append(n // i)
        i += 1
    rev.reverse()
    A = A + rev
    A.append(n)
    return A\
    
def prime(n):
    if n <= 1:return False
    i = 2
    while i*i < n:
        if n%i == 0:
            print(i)
            return False
        i += 1
    return True

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True  
    if n % 2 == 0 or n % 3 == 0:
        return False 
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  
    return True

def hcf(a,b):
    c = a%b
    if c == 0:return b
    if a%c == 0 and b%c == 0: return c
    if a%(c//2) == 0 and b%(c//2) == 0:return c//2
    for i in range(c//2, 0,-1):
        if a%i == 0 and b%i== 0:
            return i
        

def euclidean_gcd(a,b):
    while b >0:
        a, b =  b, a%b
    return a

if __name__ == '__main__':
    #print(countnrev(12345))
    #n = 1234321
    #print(f"{n} is palendrome: {palendrome(n)}")
    #arms = 9474
    #print(f"{arms} is armstrong: {armstrongno(arms)}")
    #print(alldivisor(11111))
    #print(method(11111))
    #print(dualdivisor(10000))
    #print(divisor(100000))
    #print(prime(113))
    #print(is_prime(1009))
    #print(hcf(18,90))
    #print(euclidean_gcd(9+9,96-6))
    print(Opalendrome('aaaaaaialphxxhplaiaaaaaa'))