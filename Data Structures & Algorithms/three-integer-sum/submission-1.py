class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        outputs = []
        for i, a in enumerate(nums):
            if a >0:
                break
            if (i>0) and (a == nums[i-1]):
                continue

            l = i + 1
            r = len(nums) - 1
            while l<r:
                cur = a + nums[l] + nums[r]
                if cur == 0:
                    outputs.append([a,nums[l], nums[r]])                    
                    l+=1
                    r-=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1                    
                elif cur>0:
                    r-=1
                else:
                    l+=1
        return outputs

