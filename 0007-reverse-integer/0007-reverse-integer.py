class Solution:
    def reverse(self, x: int) -> int:
       res=0
       sign=1
       if x<0:
        sign=-1
       y=abs(x)
       while y:
         bck=y//10
         frnt=y%10
         res=(res*10)+frnt
         y=bck
       res=res*sign
       if res>(2**31)-1 or res<-2**31:
        return 0
       else:
        return res 



        