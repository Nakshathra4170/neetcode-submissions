class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for item in strs:
            s+=str(len(item))+'#'+item
        return s

    def decode(self, s: str) -> List[str]:
        pairs=[]
        i=0
        while i<len(s):
            
            j=s.find('#',i)
            length=int(s[i:j])
            word=s[j+1:j+1+length]
            i=j+1+length
            pairs.append(word)
        return pairs
