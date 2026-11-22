class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack=[] # index,hight
        area=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                idx,high=stack.pop()
                area=max(area,high*(i-idx))
                start=idx
            stack.append([start,h])
        for i,h in stack:
            area=max(area,h*(len(heights)-i))
        return area
            
        