class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #nlogn sol
        if len(nums)<=1:
            return len(nums)
        nums = sorted(set(nums))
        max_length = 1
        cur_head = 0
        for i in range(len(nums)-1):            
            if (nums[i+1] - nums[i])==1:
                continue                
            else:
                max_length = max(max_length, i+1 - cur_head)
                cur_head = i+1
        max_length = max(max_length, len(nums)-cur_head)            
        return max_length