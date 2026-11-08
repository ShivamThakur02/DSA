class Solution:
    def trap(self, height: list[int]) -> int:
        res=0
        leftmax,rightmax=0,0
        l,r=0,len(height)-1
        while l<r:
            if height[l]<height[r]:
                leftmax=max(leftmax,height[l])
                res+=leftmax-height[l]
                l+=1
            else:
                rightmax=max(rightmax,height[r])
                res+=rightmax-height[r]
                r-=1
        return res