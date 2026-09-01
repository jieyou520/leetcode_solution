#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        cap = 0
        leftCeil, rightCeil = 0, 0

        while l <= r:
            leftCeil = max(leftCeil, height[l])
            rightCeil = max(rightCeil, height[r])

            if leftCeil < rightCeil:
                cap += leftCeil - height[l] 
                l += 1  
            else:
                cap += rightCeil - height[r] 
                r -= 1 

        return cap    
# @lc code=end

