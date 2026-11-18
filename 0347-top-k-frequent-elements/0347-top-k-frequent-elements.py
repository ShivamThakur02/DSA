class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        sorted_items=dict(sorted(freq.items(),key=lambda x:x[1],reverse=True))
        return list(sorted_items.keys())[:k]
