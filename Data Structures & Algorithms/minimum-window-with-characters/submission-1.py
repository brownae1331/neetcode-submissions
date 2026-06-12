class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1

        res = ""
        for l in range(len(s)):
            substring = ""
            ssCount = {}
            r = l
            if tCount.get(s[l], 0) > 0:
                substring += s[l]
                ssCount[s[l]] = ssCount.get(s[l], 0) + 1

                while r < len(s) - 1 and tCount != ssCount:
                    r += 1
                    if tCount.get(s[r], 0) > 0:
                        ssCount[s[r]] = ssCount.get(s[r], 0) + 1
                    substring += s[r]
                
                equal = True
                for key, value in tCount.items():
                    if ssCount.get(key, 0) < value:
                        equal = False

                if equal and (not res or len(res) > len(substring)):
                    res = substring
        return res