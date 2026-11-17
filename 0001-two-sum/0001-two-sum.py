class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dct={}
        for i in range(len(nums)):
            find=target-nums[i]
            if find in dct:
                return (i,dct[find])
            dct[nums[i]]=i
            