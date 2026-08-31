class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i,num in enumerate(nums):
            c = target - num
            if c in seen:
                return[seen[c],i]
            seen[num] = i
