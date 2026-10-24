class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dct={}
        for key in nums:
            dct[key]=dct.get(key,0)+1
        sorted_items=sorted(dct.items(),key=lambda x:x[1],reverse=True)

        return [value[0] for value in sorted_items[:k]]