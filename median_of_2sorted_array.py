class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        length = len(nums1)+len(nums2)
        result_a = result_b = None
        median = length//2
        if length%2 == 0:
            x = median +1
        else:
            median +=1
            x = median
        i = j = index = 0

        while index < x:
            index += 1
            
            if i >= len(nums1):
                candidate = nums2[j]
                j+=1
            elif j>= len(nums2):
                candidate = nums1[i]
                i+=1
            elif nums1[i] <= nums2[j]:
                candidate = nums1[i]
                i+=1
            else:
                candidate = nums2[j]
                j+=1

            if index == median:
                result_a = candidate
            if index == x:
                result_b = candidate 
                return (result_a + result_b)/2.0
            
        return None


if __name__ == "__main__":
    solver = Solution()
    
    example_nums_1 = [1,2,3,4,5]
    example_nums_2 = [6,7,8,9,10,11,12,13,14,15,16,17]
    
    
    result = solver.findMedianSortedArrays(example_nums_1, example_nums_2)
    print("Output indices:", result)  
