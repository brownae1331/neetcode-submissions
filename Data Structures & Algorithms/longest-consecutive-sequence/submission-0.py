class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 in numSet:
                continue
            x = num
            l = 0
            while x in numSet:
                l += 1
                x += 1
            if l > longest:
                longest = l
        return longest