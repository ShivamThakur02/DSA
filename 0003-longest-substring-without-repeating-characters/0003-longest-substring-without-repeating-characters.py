class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique=set()
        prev_max=0
        l,r=0,0
        while r<len(s):
            if s[r] not in unique:
                unique.add(s[r])
                prev_max=max(prev_max,r-l+1)
                r+=1
            else:
                unique.remove(s[l])
                l+=1
        return prev_max