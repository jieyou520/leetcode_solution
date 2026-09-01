#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        if len(nums) != 1:
            for i in range(0,len(nums)-1):
                if nums[i+count] == 0:
                    nums.pop(i+count)
                    nums.append(0)
                    count -= 1
        return nums
        
        
# @lc code=end

