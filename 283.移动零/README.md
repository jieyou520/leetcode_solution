# [283] 移动零

- **LeetCode 链接**: [移动零](https://leetcode.cn/problems/move-zeroes/)
- **难度**: Easy
- **标签**: `#数组` `#双指针`

## 题目描述

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。要求必须在原数组上操作，不能拷贝额外数组。

## 思路

1. **核心思想**：遍历数组时把遇到的 `0` 从当前位置移除并追加到数组末尾，保持非零元素的相对顺序不变。
2. **思考过程**：直接删除元素会让后续下标变化，因此用一个计数器修正当前检查位置；另一种常见做法是用双指针把非零元素依次前移。
3. **关键点**：所有操作都在原数组上完成；移动后要保证剩余的非零元素仍然按原来的相对顺序排列。

## 解法

### 方法一：原地移除并追加
* **思路**：从头遍历数组，遇到 `0` 就弹出该元素并追加到末尾，同时调整当前遍历位置。
* **代码**：
    ```python
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
    ```
