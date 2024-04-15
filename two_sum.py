import copy
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        i = 0
        while nums:
            n = nums.pop(0)

            for j, p in enumerate(nums):
                
                if n+p == target:
                    return [i,i+j+1]
            i += 1