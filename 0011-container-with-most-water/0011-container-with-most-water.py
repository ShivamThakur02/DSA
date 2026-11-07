class Solution:
    def maxArea(self, height: list[int]) -> int:
        l,r=0,len(height)-1
        res=0
        while l<r:
            length=min(height[l],height[r])
            area=length*(r-l)
            res=max(area,res)
            if height[r]<height[l]:
                r-=1
            else:
                l+=1
        return res

        