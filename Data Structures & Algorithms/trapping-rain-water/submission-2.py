class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax = 0
        rmax = 0
        total_area = 0
        while(l<r):
            if height[l]<=height[r]:
                if lmax < height[l]:
                    lmax = height[l]
                else:
                    total_area += (lmax-height[l])
                l+=1
            else:
                if rmax < height[r]:
                    rmax = height[r]
                else:
                    total_area += (rmax-height[r])
                r-=1
        return total_area
