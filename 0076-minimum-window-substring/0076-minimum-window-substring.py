class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash1,hash2={},{}
        for i in range(len(t)):
            hash1[t[i]]=hash1.get(t[i],0)+1
        have,want=0,len(set(t))
        res,reslen=[-1,-1],float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            hash2[c]=hash2.get(c,0)+1

            if c in hash1 and hash2[c]==hash1[c]:
                have+=1
            
            while have==want:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1

                hash2[s[l]]-=1
                if s[l] in hash1 and hash2[s[l]]<hash1[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!=float("infinity") else ""
            

        