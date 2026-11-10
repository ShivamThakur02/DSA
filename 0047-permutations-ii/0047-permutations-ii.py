class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res=[]
        dct=dict()
        for i in nums:
            dct[i]=dct.get(i,0)+1
        def backtrack(stack):
            if len(stack)==len(nums):
                res.append(stack[:])
                return 
            for i in dct:
                if dct[i]>0:
                    stack.append(i)
                    dct[i]-=1
                    backtrack(stack)
                    dct[i]+=1
                    stack.pop()
        backtrack([])
        return res