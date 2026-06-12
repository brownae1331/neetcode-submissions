class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 1, len(numbers)
        while l < r:
            res = numbers[l-1] + numbers[r-1]
            if res < target:
                l += 1
            elif res > target:
                r -= 1
            else:
                return [l, r]
        return []