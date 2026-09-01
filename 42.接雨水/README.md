# [42] 接雨水

- **LeetCode 链接**: [接雨水](https://leetcode.cn/problems/trapping-rain-water/)
- **难度**: Hard
- **标签**: `#数组` `#双指针`

## 题目描述

给定 `n` 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子下雨之后能接多少雨水。

## 思路

1. **核心思想**：某个位置能接的水量等于它左右两边最大高度中的较小值减去当前高度，用双指针从两端向中间计算。
2. **思考过程**：暴力解需要为每个位置分别求左右最大高度。双指针从两端移动时，可以只维护已经扫过部分的最高高度，一次遍历完成计算。
3. **关键点**：每次移动较矮一侧的指针，并用当前侧的已知最大高度计算积水量；两个方向的最大高度分别用 `leftCeil` 和 `rightCeil` 维护。

## 解法

### 方法一：双指针
* **思路**：左右指针从两端向中间移动，维护两侧的最大高度，每次按较矮一侧能承接的水量累加。
* **代码**：
    ```python
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
    ```
