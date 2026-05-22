class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()

        for x in nums:
            if x not in hashmap:
                hashmap.add(x)

            else:
                return True
        
        return False

        
        