class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in (num1,num2):
            return "0"
        n=len(num1)
        m=len(num2)
        res=[0]*(m+n)
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                multi=int(num1[i])*int(num2[j])
                total=multi+res[i+j+1]
                res[i+j+1]=total%10
                res[i+j]+=total//10
        zero=0
        while zero<len(res) and res[zero]==0:
            zero+=1
        res2=map(str,res[zero:])
        res3="".join(res2)
        return res3

        