class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numlist = {}
        for i,n in enumerate(nums):
            if target - n in numlist:
                return [i, numlist[target - n]]
            numlist[n] = i 