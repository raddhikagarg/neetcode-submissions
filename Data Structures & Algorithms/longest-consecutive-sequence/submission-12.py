class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = list(set(nums))
        num.sort()
        
        l = len(num)
        if l != 0:
            count = 1
            max_count = 1
            for i in range(0,l-1,1):
                if num[i+1] == num[i] + 1:
                    count += 1
                    if count > max_count:
                        max_count = count
                else:
                    count = 1
        if l ==1:
            max_count = 1
        if l == 0:
            max_count = 0
        return max_count
            

        