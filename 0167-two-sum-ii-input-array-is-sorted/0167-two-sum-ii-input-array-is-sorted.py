class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]+nums[r]>target:
                r-=1
            elif nums[l]+nums[r]<target:
                l+=1
            else:
                return[l+1,r+1]
            