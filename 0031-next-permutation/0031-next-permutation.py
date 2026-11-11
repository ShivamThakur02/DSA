class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            return nums.reverse()
        pivot = i - 1
        j = len(nums) - 1
        while nums[j] <= nums[pivot]:
            j -= 1
        nums[pivot], nums[j] = nums[j], nums[pivot]
        nums[i:] = reversed(nums[i:])
            
                