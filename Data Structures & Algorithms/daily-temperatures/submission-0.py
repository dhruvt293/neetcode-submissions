class Solution:
    def dailyTemperatures(self, temp: List[int]):
        stack = []
        ans = [0]*len(temp)

        for x in range(len(temp)-1,-1,-1):
            while stack and temp[x] >= temp[stack[-1]]:
                stack.pop()
            if stack:
                ans[x] = stack[-1]-x
            stack.append(x)
        return ans