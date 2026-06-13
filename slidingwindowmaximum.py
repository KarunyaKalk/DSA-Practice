import typing 

class Solution:
    def maxSlidingWindow(self, nums: typing.List[int], k: int) -> typing.List[int]:
        res=[]
        n=len(nums)
        for i in range(n-k+1):
            mx=nums[i]
            for j in range(k):
                mx=max(mx,nums[i+j])
            res.append(mx)
        return res
        