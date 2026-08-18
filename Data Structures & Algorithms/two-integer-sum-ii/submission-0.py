class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        result=[]
        while i<j:
            sum=numbers[i]+numbers[j]
            if sum>target:
                j-=1
            elif sum==target:
                result.extend([i+1,j+1])
                return result

            else:
                i+=1