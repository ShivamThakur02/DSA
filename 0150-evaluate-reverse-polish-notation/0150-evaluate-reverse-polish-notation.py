class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            else:
                a=stack.pop()
                a=int(a)
                b=stack.pop()
                b=int(b)
                if i=="+":
                    stack.append(a+b)
                if i=="-":
                    stack.append(b-a)
                if i=="*":
                    stack.append(b*a)
                if i=="/":
                    stack.append(b/a)
        return int(stack[-1])
                    