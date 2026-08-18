class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current=0
        maximum=0
        i=0
        j=len(heights)-1
        while i<j:
            h=min(heights[i],heights[j])
            b=j-i
            current=b*h
            if current>maximum:
                maximum=current
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maximum