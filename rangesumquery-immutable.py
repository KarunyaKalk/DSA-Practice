from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for i in nums:
            x=self.prefix[-1]+i
            self.prefix.append(x)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1]-self.prefix[left]
        