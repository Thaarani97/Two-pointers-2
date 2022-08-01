#Approach - 1
#TC :O(n)
#SC :O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums.clear()
        for k,v in count.items():
            if v>=2:
                nums.append(k)
                nums.append(k)
            else:
                nums.append(k)
        
        return len(nums)

#Approach - 2
#TC :O(n)
#SC :O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        count = 1
        
        for fast in range(1,len(nums)):
            if nums[fast] == nums[fast-1]:
                count+=1
            else:
                count=1
                
            if count<=2:
                nums[slow] = nums[fast]
                slow+=1
        
        return slow