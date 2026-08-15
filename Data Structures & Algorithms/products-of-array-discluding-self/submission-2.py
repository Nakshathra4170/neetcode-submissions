class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro=1
        output=[]
        left=0

        while left<len(nums):
            output.append(pro)
            pro*=nums[left]
            left+=1
        right=len(output)-1
        mul=1
        while right>=0:
            output[right]*=mul
            mul*=nums[right]
            right-=1
        return output
        