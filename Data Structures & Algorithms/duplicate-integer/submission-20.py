class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nos = []
        for i in nums:
            if i in nos:
                return True
            else: nos.append(i)
        return False
        
        
                
