class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for item in strs:
            key=''.join(sorted(item))
            if key not in freq:
                freq[key]=[]
            freq[key].append(item)
        return list(freq.values())
        