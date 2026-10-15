class Solution:
    def reverseWords(self, s: str) -> str:
        s=s[::-1]
        s=s.strip()
        i=0
        res=""
        temp=""
        while i<len(s):
            if s[i]!=" ":
                temp+=s[i]
            elif s[i]==" " and temp!="":
                temp=temp[::-1]
                res+=temp
                res+=" "
                temp=""
            i+=1
        res+=temp[::-1]
        return res                
