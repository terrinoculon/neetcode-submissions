class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        output = []
        prefix_prod = 1
        suffix_prod = 1
        length = len(nums)
        for i in range(length):
            if i>0:            
                prefix_prod *= nums[i-1]
            prefix.append(prefix_prod)            
            suffix.append(suffix_prod)
            if i<(length - 1):
                suffix_prod *= nums[length -i -1]                        
        for i in range(length):
            output.append(prefix[i] * suffix[length -i-1])
        return output
