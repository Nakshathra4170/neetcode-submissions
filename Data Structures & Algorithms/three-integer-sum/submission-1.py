class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for k in range(len(nums)):
            if k>0 and nums[k]==nums[k-1]:
                continue
            i=k+1
            j=len(nums)-1
            while i<j:
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    result.append([nums[i],nums[j],nums[k]])
                    i+=1
                    j-=1
                    while i<j and nums[i]==nums[i-1]:
                         i+=1
                    while i<j and nums[j]==nums[j+1]:
                         j-=1
                elif sum>0:
                    j-=1
                else:
                    i+=1
        return result
        