class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c,0) + 1
        left = 0
        count  = len(t)
        ans = ""

        for right , c in enumerate(s):
            if c in need:
                if need[c]>0:
                    count -= 1
                need[c] -=1
            while count ==0:
                 if not ans or right - left + 1 < len(ans):
                    ans = s[left:right+1]
                 if s[left] in need:
                    need[s[left]] +=1
                    if need [s[left]]>0:
                        count +=1
                 left +=1
        return ans

        