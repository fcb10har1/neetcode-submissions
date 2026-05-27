class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_set = {}
        t_set = {}

        for n in s:
            s_set[n] = s_set.get(n,0) + 1

        for n in t:
            t_set[n] = t_set.get(n,0) + 1

        return t_set == s_set
                

        