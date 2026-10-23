class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dct={}
        for i in strs:
            key="".join(sorted(i))
            if key in dct:
                dct[key].append(i)
            else:
                dct[key]=[i]

        return list(dct.values())        