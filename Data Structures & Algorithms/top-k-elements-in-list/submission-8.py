class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        array = [[] for i in range(len(nums)+1)]

        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1 

        for key,value in hashmap.items():
            array[value].append(key)

        res = []
        for i in range(len(array)-1,-1,-1):
            for n in array[i]:
                res.append(n)
                if len(res) == k:
                    return res
                


        