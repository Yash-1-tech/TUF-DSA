
def sqpattern(n):
    for i in range(n):
        for j in range(n):
            print('#', end='')
        print()

def slop(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end ="")
        print()

def slopjcount(n):
    for i in range(n+1):
        for j in range(i):
            print(j+1, end ='')
        print()

def slopicount(n):
    for i in range(n+1):
        for j in range(i):
            print(i, end ="")
        print()

def reverseslop(n):
    for i in range(n):
        for j in range(n-i):
            print(n-i, end='')
        print()

def revseslopicount(n):
    for i in range(n):
        for j in range(n-i):
            print(n-i-j, end='')
        print()

def pyramid(n):
    for i in range(n):
        for j in range(n):
            if i==0 and n/2-1/2< j <= n/2+1/2:
                print(j,i, end ="")
            elif n/2-i/2<= j <= n/2+i/2:
                print(j,i, end="")
            else:
                print(end="_")
        print()

if __name__ == '__main__':
    n = int(input("give me the length of sqaure pattern "))
    slop(n)
    print()
    slopjcount(n)
    print()
    slopicount(n)
    print()
    sqpattern(n)
    print()
    reverseslop(n)
    print()
    revseslopicount(n)
    print()
    pyramid(n)
    print()
    print('done')
