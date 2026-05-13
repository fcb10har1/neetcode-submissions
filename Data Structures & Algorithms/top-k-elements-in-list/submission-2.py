class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        ans = []
        
        # This just added all the ints to a hashmap
        for i in nums:
                map[i] = map.get(i,0) + 1

        while k != 0:
            max_freq = 0
            max_key = 0
            for key in map:
                if map[key] > max_freq:
                    max_key = key
                    max_freq = map[key]

            ans.append(max_key)
            del map[max_key]
            k -= 1
        return ans





        