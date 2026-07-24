class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid]<nums[0] and nums[mid-1]>nums[mid]:
                return nums[mid]
            elif nums[mid]<nums[0]:
                r = mid - 1
            else:
                l = mid + 1
        return nums[0]
