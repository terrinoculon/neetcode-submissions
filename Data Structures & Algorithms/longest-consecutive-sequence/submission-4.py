class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        max_length = 0
        for num in nums:
            if not mp[num]:
                mp[num] = mp[num-1] + mp[num+1] +1
                mp[num-mp[num-1]] = mp[num]
                mp[num+mp[num+1]] = mp[num]
                max_length = max(max_length, mp[num])
        return max_length
