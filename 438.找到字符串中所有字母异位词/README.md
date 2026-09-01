# [438] 找到字符串中所有字母异位词

- **LeetCode 链接**: [找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)
- **难度**: Medium
- **标签**: `#字符串` `#哈希表` `#滑动窗口`

## 题目描述

给定两个字符串 `s` 和 `p`，在 `s` 中找到所有 `p` 的异位词的子串，返回这些子串的起始索引。

## 思路

1. **核心思想**：用固定长度的滑动窗口维护 `s` 中与 `p` 等长的子串，并用字符计数比较窗口内容是否和 `p` 的字符组成相同。
2. **思考过程**：暴力解会为每个可能的起点重新统计窗口，时间复杂度高。滑动窗口只需要在右端加入新字符、在左端移除旧字符，即可 O(1) 增量更新计数。
3. **关键点**：窗口长度始终为 `len(p)`；比较两个 `Counter` 相等时记录左端下标，然后移除窗口最左侧字符为下一轮做准备。

## 解法

### 方法一：滑动窗口 + 哈希计数
* **思路**：维护 `s` 中长度等于 `len(p)` 的窗口计数，和 `p` 的计数相等时记录窗口起点。
* **代码**：
    ```python
    class Solution:
        def findAnagrams(self, s: str, p: str) -> List[int]:
            cnt_p = Counter(p)
            cnt_s = Counter()
            ans = []

            for right, c in enumerate(s):
                cnt_s[c] += 1

                left = right - len(p) + 1
                if left < 0:
                    continue

                if cnt_s == cnt_p:
                    ans.append(left)

                cnt_s[s[left]] -= 1

            return ans
    ```
