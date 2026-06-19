class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_locations = {}
        for i in range(len(nums)):
            if nums[i] in diff_locations:
                return [diff_locations[nums[i]], i]
            diff_locations[target - nums[i]] = i
        return []