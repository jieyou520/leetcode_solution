# [11] 盛最多水的容器

- **LeetCode 链接**: [盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/)
- **难度**: Medium
- **标签**: `#数组` `#双指针`

## 题目描述

给定一个长度为 `n` 的整数数组 `height`，其中每个元素代表坐标 `(i, height[i])` 处的一条垂直线。找出其中的两条线，使它们与 `x` 轴共同构成的容器可以容纳最多的水，返回容器可以储存的最大水量。

## 思路

1. **核心思想**：用左右两个指针从数组两端向中间移动，容器的容量由较短的一边和宽度决定，因此每次移动较短的一边。
2. **思考过程**：暴力解是枚举所有左右边界组合，时间复杂度为 O(n^2)。双指针每次都能排除一批不可能更大的组合，把复杂度降到 O(n)。
3. **关键点**：宽度减少时只有提高较短边的高度才可能让容量变大；记录并更新遍历过程中的最大面积。

## 解法

### 方法一：双指针
* **思路**：左右指针分别指向数组两端，计算当前容器的面积并记录最大值；比较两边高度，移动较矮的一侧继续计算。
* **代码**：
    ```python
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
    ```
