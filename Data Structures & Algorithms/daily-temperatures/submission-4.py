class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #(temp, i)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                StackTemp, StackInd = stack.pop()
                res[StackInd] = (i - StackInd)
            stack.append([t,i])

        return res