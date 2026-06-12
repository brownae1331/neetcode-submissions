class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if not stack:
                stack.append((i, temperatures[i]))
                continue

            while stack and temperatures[i] > stack[-1][1]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            else:
                stack.append((i, temperatures[i]))
        return res