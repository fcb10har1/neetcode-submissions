class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hashmap = collections.defaultdict()
        for i,n in enumerate(nums):
            hashmap[n] = i
            if n == target:
                return i
        else:
            return -1