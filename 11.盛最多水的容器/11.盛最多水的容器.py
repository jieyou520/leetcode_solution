#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_max = []
        x = len(height)-1
        count_right = len(height)-1
        count_left = 0
        area1 = min(height[0],height[-1])*x
        l_max.append(area1)
        for i in range(0,len(height)-1):
            if height[count_left] <= height[count_right]:
                count_left += 1
                x -= 1
                area = min(height[count_left],height[count_right])*x
                l_max.append(area)
            else:
                count_right -= 1
                x -= 1
                area = min(height[count_left],height[count_right])*x
                l_max.append(area)
        return max(l_max)

# @lc code=end

