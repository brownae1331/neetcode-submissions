class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0] * 26
        for c in s1:
            s1Count[ord(c) - ord("a")] += 1
        
        l = 0
        ssCount = [0] * 26
        for r in range(len(s2)):
            ssCount[ord(s2[r]) - ord("a")] += 1

            if r - l + 1 < len(s1):
                continue

            if ssCount != s1Count:
                ssCount[ord(s2[l]) - ord("a")] -= 1
                l += 1
            else:
                return True
        return False