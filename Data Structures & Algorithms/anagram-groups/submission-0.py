class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)

        for n in strs:
            index = [0] * 26
            for c in n:
                index[ord(c) - ord("a")] += 1

        
            hashmap[tuple(index)].append(n)
        
        return list(hashmap.values())

        


        