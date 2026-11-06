class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        candidates.sort()
        def backtrack(idx,total,stack):
            if total==target:
                res.append(stack[:])
                return
            if total>target or idx==len(candidates):
                return
            stack.append(candidates[idx])
            backtrack(idx+1,total+candidates[idx],stack)
            stack.pop()
            while idx+1<len(candidates) and candidates[idx]==candidates[idx+1]:
                idx+=1
            backtrack(idx+1,total,stack)
        backtrack(0,0,[])
        return res