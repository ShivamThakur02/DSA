class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(stack):
            if len(stack) == len(nums):
                res.append(stack[:])
                return
            for i in range(len(nums)):
                if nums[i] in stack:
                    continue
                stack.append(nums[i])
                backtrack(stack)
                stack.pop()
        backtrack([])
        return res
