class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix=prefix*nums[i]
        suffix=1
        for j in range(len(nums)-1,-1,-1):
            res[j]=res[j]*suffix
            suffix=suffix*nums[j]

        return res
        