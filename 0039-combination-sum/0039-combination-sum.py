class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        def backtrack(idx,total,stack):
            if total==target:
                res.append(stack[:])
                return
            if total>target or idx==len(candidates):
                return
            stack.append(candidates[idx])
            backtrack(idx,total+candidates[idx],stack)
            stack.pop()
            backtrack(idx+1,total,stack)
        backtrack(0,0,[])
        return res
        