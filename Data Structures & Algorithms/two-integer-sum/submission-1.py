class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_locations = {}
        for i, n in enumerate(nums):
            if n in diff_locations:
                return [diff_locations[n], i]
            diff_locations[target - n] = i
        return []