# [1] 两数之和

- **LeetCode 链接**: [两数之和](https://leetcode.cn/problems/two-sum/)
- **难度**: Easy
- **标签**: `#数组` `#哈希表`

## 题目描述

给定一个整数数组 `nums` 和一个整数目标值 `target`，在数组中找出和为目标值的两个整数，并返回它们的数组下标。假设每种输入只会对应一个答案，且同一个元素不能使用两次。

## 思路

1. **核心思想**：利用哈希表存储已遍历的元素及其索引，在遍历时检查 `target - nums[i]` 是否已经出现过。
2. **思考过程**：暴力解是枚举每一对 `(i, j)`，时间复杂度为 O(n^2)。哈希表可以把查找补数的时间从 O(n) 降到 O(1)，只需要一次遍历。
3. **关键点**：先查找补数再写入当前元素，避免同一个元素被使用两次；哈希表的键为元素值，值为元素下标。

## 解法

### 方法一：哈希表
* **思路**：一次遍历，用字典保存已经见过的数字和下标；每遇到一个数字就检查 `target - num` 是否已经在字典中。
* **代码**：
    ```python
    class Solution(object):
        def twoSum(self, nums, target):
            seen = {}
            for i,num in enumerate(nums):
                c = target - num
                if c in seen:
                    return[seen[c],i]
                seen[num] = i
    ```
