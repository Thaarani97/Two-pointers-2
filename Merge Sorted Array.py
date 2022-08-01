
#Approach - 1
#TC :O(n+m)
#SC :O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        p3 = m+n-1
        
        while p1>=0 and p2>=0:
            if nums1[p1]>nums2[p2]:
                nums1[p3]=nums1[p1]
                p1-=1
            else:
                nums1[p3]=nums2[p2]
                p2-=1
            p3-=1
            
        if p2>=0:
            nums1[:p2+1]=nums2[:p2+1]

#Approach - 2
#TC :O((n+m)log(n+m))
#SC :O(n)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums2_len = len(nums1) - len(nums2)
        print(nums2_len)
        print(len(nums1))
        j = 0
        
        for i in range(nums2_len,len(nums1)):
            nums1[i] = nums2[j]
            j = j+1
            
        return nums1.sort()