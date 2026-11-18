class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sets=set(nums)
        res=0
        for i in sets:
            if i-1 not in sets:
                count=1
                while (i+1) in sets:
                    count+=1
                    i+=1
                res=max(res,count)
        return res