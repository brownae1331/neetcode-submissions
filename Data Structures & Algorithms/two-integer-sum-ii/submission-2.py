class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 1
        r = len(numbers)

        while numbers[l-1] + numbers[r-1] != target:
            if numbers[l-1] + numbers[r-1] > target:
                r -= 1
            else:
                l += 1
        return [l, r]