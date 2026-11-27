class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique=set()
        l,r=0,0
        res=0
        while r<len(s):
            if s[r] not in unique:
                unique.add(s[r])
                res=max(res,r-l+1)
                r+=1
            else:
                unique.remove(s[l])
                l+=1
        return res