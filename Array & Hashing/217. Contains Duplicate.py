class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for i in nums:
            if m.get(i):
                return True
            else: m[i] = 1
        
        return False
                

#------------------------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) !=  len(nums)