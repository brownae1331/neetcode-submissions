class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = False
        nums2 = []
        for x in nums:
            for y in nums2:
                if x == y:
                    output = True
            nums2.append(x)
        return output