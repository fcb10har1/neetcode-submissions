class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        array = [[] for i in range(len(nums) + 1)]
        

        for n in nums:
            hmap[n] = hmap.get(n,0) + 1
        
        for h,v in hmap.items():
            array[v].append(h)
        res = []
        for i in range(len(array)-1,-1,-1):
            for j in array[i]:
                res.append(j)
                if len(res) == k:
                    return res
                    


        

        