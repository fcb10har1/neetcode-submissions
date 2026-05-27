class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = collections.defaultdict(int)


        for n,v in enumerate(nums):
            if target-v in hashmap:
                return [hashmap[target - v], n]
            else:
                hashmap[v] = hashmap.get(v,0) + n

    
        