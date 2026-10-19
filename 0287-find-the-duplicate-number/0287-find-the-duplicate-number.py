class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        l,r=0,0
        while True:
            l=nums[l]
            r=nums[nums[r]]
            if l==r:
                break
        l=0
        while True:
            l=nums[l]
            r=nums[r]
            if l==r:
                return r