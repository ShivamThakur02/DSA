class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sets=set(nums)
        largest=0
        for  i  in sets:
            if (i-1) not in sets:
                c=1
                while(i+1) in sets:
                    c+=1
                    i+=1
                largest=max(largest,c)
        return largest
        