def element(row, column):
    def worker(i,j):
        if j <= 1:
            return i
        return i* worker(i-1,j-1)

    return worker(row-1,column-1)//worker(column-1,column-1)

def for_element(row, column):
    result = 1

    for i in range(column-2):
        result *= (row-1)//i
        
    return result
    
          

print(element(10,3))
print(for_element(10,3))
