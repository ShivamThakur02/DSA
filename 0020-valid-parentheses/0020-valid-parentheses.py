class Solution:
    def isValid(self, s: str) -> bool:
       stack=[]
       result=""
       for i in s:
        if i=="(" or i=="[" or i=="{":
            stack.append(i)
        elif stack and ((i==")" and stack[-1]=="(") or (i=="]" and stack[-1]=="[") or (i=="}" and stack[-1]=="{")):
            stack.pop()
        else: return False
       return len(stack)==0