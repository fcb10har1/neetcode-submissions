class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        array = [[] for i in range(len(nums) + 1)]

        for num in nums:
            map[num] = map.get(num,0) + 1

        for c,v in map.items():
            array[v].append(c)

        res = []
        for i in range(len(array)-1,0, -1):
            for num in array[i]:
                res.append(num)
                if len(res) == k:
                    return res