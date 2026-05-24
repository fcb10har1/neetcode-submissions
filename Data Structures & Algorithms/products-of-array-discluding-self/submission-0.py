class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i,n in enumerate(nums):
            old_i = i
            i = (i + 1) % len(nums)
            value = 1
            while i != old_i:
                value *= nums[i]
                i = (i + 1) % len(nums)
            
            res.append(value)

        return res
        
        

        

