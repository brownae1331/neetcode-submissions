class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dsf(i) -> int:
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dsf(i+1), nums[i] + dsf(i+2))
            return memo[i]
        return dsf(0)