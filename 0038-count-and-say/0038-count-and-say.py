class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        res=""
        prev=self.countAndSay(n-1)
        i=0
        while i<len(prev):
            c=1
            while i+1<len(prev) and  prev[i]==prev[i+1]:
                c+=1
                i+=1
            res+=str(c)+prev[i]
            i+=1
        return  res 
        