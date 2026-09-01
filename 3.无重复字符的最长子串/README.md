# [3] 无重复字符的最长子串

- **LeetCode 链接**: [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
- **难度**: Medium
- **标签**: `#哈希表` `#字符串` `#滑动窗口`

## 题目描述

给定一个字符串 `s`，找出其中不含有重复字符的最长子串的长度。

## 思路

1. **核心思想**：用哈希表记录每个字符最近一次出现的位置，用动态规划维护以当前字符结尾的最长无重复子串长度。
2. **思考过程**：暴力解需要枚举所有子串并检查是否重复。用哈希表保存字符位置后，可以 O(1) 得到上一个相同字符的位置，从而递推当前最长长度。
3. **关键点**：`tmp` 表示以 `s[j]` 结尾的最长无重复子串长度；当出现重复字符时，新的长度不能超过 `j - i`。

## 解法

### 方法一：哈希表 + 动态规划
* **思路**：遍历字符串，记录每个字符最近出现的下标，并根据 `j - i` 和上一轮长度递推当前无重复子串长度。
* **代码**：
    ```python
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            dic = {}
            res = tmp = 0
            for j in range(len(s)):
                i = dic.get(s[j], -1)
                dic[s[j]] = j
                tmp = tmp + 1 if tmp < j - i else j - i
                res = max(res, tmp)
            return res
    ```
