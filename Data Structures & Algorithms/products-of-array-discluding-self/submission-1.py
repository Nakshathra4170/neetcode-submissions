class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        pro=1
        i=0
        
        while i<len(nums):
           output.append(pro)
           pro*=nums[i]
           i+=1
        right=1
        j=len(output)-1
        while j>=0:
            output[j]*=right
            right*=nums[j]
            j-=1
        return output


            
            
        