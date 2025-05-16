class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset[num] = 1
        return False