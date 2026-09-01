# [128] 最长连续序列

- **LeetCode 链接**: [最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/)
- **难度**: Medium
- **标签**: `#数组` `#哈希表`

## 题目描述

给定一个未排序的整数数组 `nums`，找出数字连续的最长序列的长度，并且要求算法的时间复杂度为 O(n)。

## 思路

1. **核心思想**：先把所有数字放入哈希集合，只从连续序列的起点开始向后扩展，避免重复统计。
2. **思考过程**：暴力解会对每个数字都向左向右查找，时间复杂度高。用集合保存元素后，查找相邻数字只需要 O(1)；只有当 `num - 1` 不存在时，`num` 才可能是连续序列的起点。
3. **关键点**：先判断 `num - 1` 是否在集合中，保证每个连续序列只被统计一次；集合可以去重，避免相同数字重复计算。

## 解法

### 方法一：哈希集合
* **思路**：遍历集合中的每个数字，如果它是连续序列的起点，就不断向后查找并更新最长长度。
* **代码**：
    ```python
    class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
            nums_set = set(nums)
            long = 0
            for num in nums_set:
                if num-1 not in nums_set:
                    corrent_num = num
                    corrent_len = 1
                    while corrent_num +1 in nums_set:
                        corrent_len += 1
                        corrent_num += 1
                    long = max(long,corrent_len)
            return long
    ```
