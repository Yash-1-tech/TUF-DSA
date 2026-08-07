
# zeros and ones
def worker(arr):
    tuple =[]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                tuple.append((i,j))

    for i, j in tuple:
        arr[i] = [0]* len(arr[i])
        for a in range(len(arr)):
            track = (a,j)
            arr[a][j] = 0

def matrices(matrix):
    n = len(matrix)
    m = len(matrix[0])
    col0 = 1
    for row in range(n):
        for column in range(m):
            if matrix[row][column] == 0:
                matrices[row][0] = 0
                if(column != 0):
                    matrix[row][0] = 0
                else:
                    col0 = 0

    for row in range(1,n):
        for column in range(1,m):
            if matrix[row][column] != 0:
                if matrix[0][column] == 0 or matrix[row][column] == 0:
                    matrix[row][column] = 0

    if matrix[0][0] == 0:
        matrix[0] = [0]*m

    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

def rotate_90(arr):
    n = len(arr)
    m = len(arr[0])
    matrix = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[j][m-i-1]=arr[i][j]
    for i in range(n):
        for j in range(m):
            arr[i][j]=matrix[i][j]

def rotate_90_O_1(arr):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(i+1,m):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
        
    for i in range(n):
        arr[i] = arr[i][::-1]

def spiral_print(arr):
    n = len(arr)
    m = mj = len(arr[0])
    for i in range(n):
        # print right
        for j in range(max(mj-m-1,0),m):
            print(arr[i][j])
        for a in range(i+1,n-1):
            print(arr[a][m-1])
        if mj - m == 0:
            for b in arr[n-1][m-1::-1]:
                print(b)
        else:
            for b in arr[n-1][m-1:mj-m:-1]:
                print(b)
        for c in range(n-2,1,-1):
            print(arr[c][i])
        n-=1
        m-=1


if __name__ == "__main__":
    arr =[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    ]
    spiral_print(arr)
    """for a in arr:
        print(a)
    rotate_90_O_1(arr)
    print()
    print()
    for a in arr:
        print(a)"""   
