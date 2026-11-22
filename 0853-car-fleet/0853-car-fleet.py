class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair=sorted(zip(position,speed))
        stack=[]
        for p,s in reversed(pair):
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)