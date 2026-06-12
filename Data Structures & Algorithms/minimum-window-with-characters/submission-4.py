class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount, windowCount = {}, {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1

        l = 0
        res = ""
        have, need = 0, len(tCount)
        for r in range(len(s)):
            windowCount[s[r]] = windowCount.get(s[r], 0) + 1
            if s[r] in tCount and windowCount[s[r]] == tCount.get(s[r], 0):
                have += 1
            
            while have == need:
                if not res or r-l+1 < len(res):
                    res = s[l:r+1]

                windowCount[s[l]] -= 1
                if s[l] in tCount and windowCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1 
        return res