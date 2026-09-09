class Solution:
    def lengthOfLongestSubstring(self,s):
        visited = {}
        i = 0
        j = 0
        res = 0

        for j in range(len(s)):
            if s[j] in visited:
                i = max(visited[s[j]],i)
            res = max(j-i+1, res)
            visited[s[j]] = j+1

        return res
        
        